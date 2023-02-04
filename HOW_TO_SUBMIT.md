# How to submit your model to SpeechIO leaderboard

## Step 1. Preparing a model-image
A **model-image** is just an **ordinary directory** with a self-contained ASR system inside. e.g.:

```
jiayu@ubuntu: tree ./a_sample_model_image

a_sample_model_image
├── docker
│   └── Dockerfile
├── assets
│   └── <runtime resources: models, configs, API credentials etc>
├── model.yaml
├── README.md
└── SBI
```

**You should follow above file names and structures strictly.**  Now let's explain these item by item.

---

### 1.1 docker/Dockerfile
`docker/Dockerfile` should define all dependencies of your ASR system.

<details><summary> cloud-API ASR Dockerfile example </summary><p>

| model_id | Dockerfile |
| -- | -- |
| aispeech_api_zh | [example](models/aispeech_api/docker/Dockerfile) |
| aliyun_api_zh | [example](models/aliyun_api/docker/Dockerfile) |
| baidu_pro_api_zh | [example](models/baidu_pro_api/docker/Dockerfile) |
| microsoft_api_zh | [example](models/microsoft_api/docker/Dockerfile) |
| sogou_api_zh | [example](models/sogou_api/docker/Dockerfile) |
| tencent_api_zh | [example](models/tencent_api/docker/Dockerfile) |
| yitu_api_zh | [example](models/yitu_api/docker/Dockerfile) |

</p></details>

<details><summary> local ASR Dockerfile example </summary><p>

| model_id | Dockerfile |
| -- | -- |
| sample_kaldi_model | [example](models/sample_kaldi_model/docker/Dockerfile) |

</p></details>

**important note**: 

You need to add **`python3`** into Dockerfile, it is required by leaderboard pipeline
```
# Ubuntu
RUN apt-get install python3
...
```

For __English__ model, please also include **`regex`** and **`pynini`**:
```
# Ubuntu
RUN apt-get install python3 python3-pip
...
RUN pip3 install pynini regex
...
```

---

### 1.2 model.yaml
```
date: 2021-04-05    # date of model-image creation
task: ASR           # have to be `ASR` for now
language: zh        # lowercase language code, e.g `en`, `zh`
sample_rate: 16000  # 8000 for telephone, 16000 for other
author: Jiayu       # your name
entity: SpeechIO    # your entity
email: leaderboard@speechio.ai  # your email
```

* You can find standard language codes in [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)

---

### 1.3 Runtime Resources
Runtime resources(*model files*, *vocabulary/lexicon*, *configs* etc) should be placed inside `assets` dir, e.g.:

```
jiayu@ubuntu: tree ./a_sample_model_image

a_sample_model_image
├── assets
    ├── asr.mdl
    ├── asr.cfg
    ...
...
└── SBI
```

---

### 1.4 SBI
* **SBI** is an **executable** implemented by submitter for ASR inference.
* **SBI** can be in any language: C/C++, Java, bash, python etc.
* **SBI** will always be invoked under model-image, so it can refer to runtime resources via relative paths, e.g. `./assets/asr.{mdl,cfg}`
* **SBI** should implement following Command Line Interface(CLI):
  ```
  ./SBI <input_audio_list> <result_dir>
  ```

  **<input_audio_list>** provides a list of <audio_id> & <audio_absolute_path> to be decoded, seperated by white space:
  ```
  SPEECHIO_ASR_ZH00001__U001 /home/dataset/SPEECHIO_ASR_ZH00001/U001.wav
  SPEECHIO_ASR_ZH00001__U002 /home/dataset/SPEECHIO_ASR_ZH00001/U002.wav
  ...
  ```
  all audio files are `16k16bit mono wave`, less than 30 secs each.

  **<result_dir>** provides a directory for **SBI** to create/read/write temporary files during decoding, and final results must be written to `<result_dir>/raw_rec.txt`:
  ```
  SPEECHIO_ASR_ZH00001__U001 I just watched the movie "The Pursuit of Happiness"
  SPEECHIO_ASR_ZH00001__U002 rock and roll like a rolling stone
  ...
  ```
  `<result_dir>/raw_rec.txt` should be _ASCII/UTF-8_ encoded.

* If recognition fails for an utterence, you can write a line with <audio_id> and empty result like this:
  ```
  SPEECHIO_ASR_ZH00001__U003  
  ```

* You don't need to worry about text normalization(cases, punctuations, numbers, interjections ...), WER/CER calculation etc. Just make sure your SBI implementation follows above specifications.

* You can debug your SBI implementation inside your model-image dir on your local machine, by feeding <input_audio_list> and <result_dir> yourself.  

---

### 1.5 README.md (optional)
We strongly recommand that you provide a markdown summary about your model, covering:

* number of parameters
* training data
* feature type
* neural net structure & topology
* objective function
* optimizer
* ...

---

## Step 2: Validate your model-image locally
2.1 Make sure you already have a tiny test set `datasets/MINI_ZH`

2.2 Move prepared model-image to your local model-zoo

  ```
  mv <prepared_model_image>  <leaderboard_repo>/models/<your_model_id>
  ```

You should pick a unique & meaningful **`model_id`** for your model, e.g.:

  ```
  speechio_kaldi_pretrain
  alphacep_vosk_en
  interspeech_xxx_paper_reproduced
  deepspeech_v1
  ```

2.3 Run a minimal validation benchmark:

  ```
  ops/benchmark  -m <your_model_id>  -d MINI_ZH
  ```

2.4 Check `results/...<your_model_id>.../{RESULTS,DETAILS}.txt` for benchmark results.

---

## Step 3: Submit your model-image
A. For cloud API models: Just create a PR, add the model-image to `models/`

B. For local models:

* Install aliyun object-storage-service binary (one-time-only installation)
  ```
  # run this in leaderboard repo
  utils/install_aliyun_oss_client.sh
  ```

* Make sure your model-image is ready inside your local model zoo:
  ```
  mv <prepared_model_image> <leaderboard_repo>/models/<your_model_id>
  ```

* Register your model-image to `models/zoo.yaml`:
  ```
  speechio_kaldi_multicn:
    url: oss://speechio-leaderboard/models/speechio_kaldi_multicn/
  ...
  ...
  <your_model_id>:
    url: oss://speechio-leaderboard/models/<your_model_id>/
  ```

* Upload your model-image to cloud model-zoo:
  ```
  ops/push -m <your_model_id>
  ```

Congrats, now everyone should be able to reproduce your ASR system via leaderboard. You can always re-run above `ops/push` command to update your model-image.

---

## Contacts
Email: leaderboard@speechio.ai
