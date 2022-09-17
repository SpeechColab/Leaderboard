# How to submit your model to SpeechIO leaderboard
## Benchmarking Pipeline Overview
![image](misc/pipeline.png)

As above figure demonstrates, a benchmark cycle contains following steps:
1. submitter prepares their model following `model-image` specification
2. submitter submits model-image to model-zoo via `ops/push`
3. submitter creates a benchmarking request by adding a benchmark config(yaml) via github pull request
4. SpeechIO invokes leaderboard pipeline on a benchmarking machine and emails final results back to submitter.

---

## Step 1. Preparing your model-image
A **model-image** is just an **ordinary directory** with a self-contained ASR system inside. e.g.:
```
jiayu@ubuntu: tree ./a_sample_model_image

a_sample_model_image
├── docker
│   └── Dockerfile
├── assets
│   └── <runtime resources, e.g. models, configs, API credentials etc>
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
1. You need to add **`python3`** into Dockerfile, it is required by leaderboard pipeline
```
# Ubuntu
RUN apt-get install python3
...
```

2. For __English__ model, please also include **`regex`** and **`pynini`**:
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
date: 2021-04-05
task: ASR
language: zh
sample_rate: 16000
author: Jiayu
entity: SpeechIO
email: leaderboard@speechio.ai
```

* `date`: date of model-image creation
* `task`: must be `ASR` for now
* `language`: lowercase language code [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes), e.g `en`, `zh`
* `sample_rate`: sample rate, 8000(telephone) / 16000(other)
* `author`: author name
* `entity`: author's entity
* `email`: author's email

---

### 1.3 README.md (optional)
We strongly recommand that you provide a markdown summary about your model, covering:

* number of parameters
* training data
* feature type
* neural net structure & topology
* objective function
* optimizer
* ...

---

### 1.4 SBI
* **SBI** is an **executable** implemented by submitter for ASR inference.
* **SBI** can be in any language: *C/C++, Java, bash, python etc.
* **SBI** code can refer to other resources(models, configs, programs/scripts etc) via relative paths under model-image dir.
* **SBI** should implement following Command Line Interface(CLI):
  ```
  ./SBI <input_audio_list> <working_dir>
  ```

* Leaderboard pipeline feeds <input_audio_list> to SBI as 1st argument: Each line contains two fields <audio_id> and <audio_absolute_path>, seperated by white space:
  ```
  SPEECHIO_ASR_ZH00001__U001 /home/dataset/SPEECHIO_ASR_ZH00001/U001.wav
  SPEECHIO_ASR_ZH00001__U002 /home/dataset/SPEECHIO_ASR_ZH00001/U002.wav
  ...
  ```
  Audio files are 16k16bit wavs, less than 30 secs each.

* Leaderboard pipeline feeds <working_dir> to SBI as 2nd argument: **SBI** can create/read/write arbitrary files inside <working_dir>, but recognition results must be written to **<working_dir>/raw_rec.txt** with _ASCII/UTF-8_ encoding, e.g.:
  ```
  SPEECHIO_ASR_ZH00001__U001 I just watched the movie "The Pursuit of Happiness"
  SPEECHIO_ASR_ZH00001__U002 rock and roll like a rolling stone
  ...
  ```

* If recognition fails for an utterence, you can write a line with <audio_id> and empty result like this:
  ```
  SPEECHIO_ASR_ZH00001__U003  
  ```

* You can debug your SBI implementation inside your model-image dir on your local machine, by feeding <input_audio_list> and <working_dir> yourself.  

* You don't need to worry about text normalization(cases, punctuations, numbers, years etc), WER/CER calculation etc. Just make sure your SBI implementation follows above specifications.

---

### 1.5 Runtime Resources
Runtime resources refers to *model files*, *configs*, *cloud-api credentials* etc. For example:

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

then SBI code can locate them via relative paths `./assets/asr.{mdl,cfg}`

---

### 1.6 Sample model-image

* a sample model-image of Cloud-API ASR system:

  https://github.com/speechio/leaderboard/tree/master/models/aispeech_api_zh

* a sample model-image of local ASR system in Kaldi framework:

  https://github.com/speechio/leaderboard/tree/master/models/sample_kaldi_model

---
### 1.7 Validate prepared model-image with leaderboard pipeline on your local machine
1. make sure you have `MINI_ZH` in your local testset-zoo `leaderboard/datasets/MINI_ZH`
2. move prepared model-image to your local model-zoo
    ```
    mv <prepared_model_image> leaderboard/models/<your_model_id>
    ```

    **`model_id`** is a unique identifier, used to refer to this model in future benchmarks.

    We let submitters to decide their model id. It should be meaningful and unique, for example:
    ```
    speechio_kaldi_pretrain
    alphacep_vosk_en
    interspeech_xxx_paper_reproduced
    deepspeech_v1
    ```
3. create a benchmark request under `leaderboard/requests/mini.yaml`, replace <your_model_id> field with your model_id:
    ```
    date: '2021-01-01'
    requester: xxx
    entity: xxx
    email: 
      - xxx@xxx.com
    model: <your_model_id>
    test_set:
      - MINI_ZH
    ```
4. run a minimal validation benchmark:
    ```
    # run this in leaderboard repo
    ops/benchmark -r requests/mini.yaml
    ```
5. check `leaderboard/results/...<your_model_id>.../{RESULTS,DETAILS}.txt`

---

## Step 2: Submitting your model-image
Just create a PR to this github repo if your model-image is based on cloud-API. 

Otherwise, for heavy-weight local ASR engine:

2.1 Install aliyun object-storage-service client (one-time-only installation)
```
# run this in leaderboard repo
utils/install_aliyun_oss_client.sh
```

2.2 Move prepared model-image dir into local model-zoo
```
mv <prepared_model_image> leaderboard/models/<model_id>  # This should have been done during local validation.
```

2.3 Register your model-image to `leaderboard/models/zoo.yaml`:
```
speechio_kaldi_multicn:
  url: oss://speechio-leaderboard/models/speechio_kaldi_multicn/
...
...
<model_id>:
  url: oss://speechio-leaderboard/models/<model_id>/
```

2.4 Upload your model-image to cloud model-zoo:
```
ops/push model <model_id>
```

Now SpeechIO/others can download/reproduce your ASR system. You can always re-run above `ops/push` command to update your model-image.

---

## Step 3: Send a benchmark request via a pull request
Once you have your model submitted, you can open a PR to this github repo, adding a request file to `requests` directory:

**`github.com/speechio/leaderboard/requests/<your_benchmark_request>.yaml`**

a sample request can be found [here](requests/sample_request.yaml):
```
date: '2021-04-05'
requester: Jiayu
entity: SpeechIO
email: 
  - xxx@gmail.com
model: aliyun_api
test_set:
  - SPEECHIO_ASR_ZH00000
  - SPEECHIO_ASR_ZH00001
```
where:
* `date`: benchmark request date
* `model`: model id, specifying which model you want to benchmark
* `test_set`: test set id list, which test sets you want to benchmark with
* `email`: a list of email addresses to receive benchmark results

you can lookup `model` and `test_set` in section 2&3 of [README](README.md)

Once we merge your submission pull request, the leaderboard pipeline will:
* init a docker runner to benchmark requested model with requested test sets
* email results to requester

## Contacts
Email: leaderboard@speechio.ai
