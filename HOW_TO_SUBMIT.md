# How to submit your model to SpeechIO leaderboard
## Benchmarking Pipeline Overview
![image](misc/pipeline.png)

As above figure demonstrates, a benchmark cycle contains following steps:
1. submitter prepares their model following `model-image` specification
2. submitter submits model-image to model-zoo via leaderboard tool
3. submitter creates a benchmarking request by adding a benchmark config(yaml) via github pull request
4. SpeechIO invokes leaderboard pipeline on a benchmarking machine and emails final results back to submitter.

---

## Step 1. Prepare a model-image
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
`docker/Dockerfile` specifies all dependencies of your system. Here, `system` can be a client of cloud-ASR, or a local ASR engine.

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

**important note**: you need to add **`python3`** in Dockerfile, because leaderboard pipeline depends on it.

---

### 1.2 model.yaml
This config list required properties of your ASR system, example below:
```
date: 2021-04-05
task: ASR
language: zh
sample_rate: 16000
author: Jiayu
entity: SpeechIO
email: leaderboard@speechio.ai
```

* `date`: date of model creation
* `task`: this field must be `ASR` for now
* `language`: language code, lowercase [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes), e.g `en`, `zh`
* `sample_rate`: sample rate, typically 8000(telephone) or 16000(other)
* `author`: author/owner
* `entity`: author/owner entity
* `email`: author/owner email

---

### 1.3 README.md (optional)
Although not mandatory, we strongly suggest that you provide a summary about your model in this markdown, such as:

* number of parameters
* amount of training data
* front end feature type
* neural net structure & topology
* objective function
* optimizer
* ...

Sharing these knowledge is benefical to the speech community.

---

### 1.4 SBI
`SBI` is an `executable`, implemented by you, for ASR inference:
* **SBI** can be written in any programming language: *C/C++, Rust, Go, Java, bash, perl, python etc* (with shebang line such as `#!/usr/bin/env bash`) 
* **SBI** will be invoked in model-image dir, so SBI code can use relative path to refer to other resources in model-image(such as models, configs, credentials, libraries, other programs/scripts)
* **SBI** needs to be able to decode an audio-list via following command line:
  ```
  ./SBI <input_audio_list> <working_dir>
  ```

* leaderboard pipeline provides <input_audio_list> to SBI as 1st argument. It is a list of 16k16bit wavs(less then 30 secs), with two fields <audio_id> and <audio_absolute_path>, seperated by whitespace:
  ```
  SPEECHIO_ASR_ZH00001__U_00001 /home/dataset/SPEECHIO_ASR_ZH00001/U_00001.wav
  SPEECHIO_ASR_ZH00001__U_00002 /home/dataset/SPEECHIO_ASR_ZH00001/U_00002.wav
  ...
  ```

  <audio_id> is a *unique* string-identifier for an audio file.

* leaderboard pipeline provides a <working_dir> to SBI as 2nd argument, **SBI** can write/read arbitrary temporary files inside, but final results must be written to **<working_dir>/raw_rec.txt**, with **ASCII/UTF-8** encoding and following format:
  ```
  SPEECHIO_ASR_ZH00001__U_00001 I just watched the movie "The Pursuit of Happiness"
  SPEECHIO_ASR_ZH00001__U_00002 rock and roll like a rolling stone
  ...
  ```

* if recognition fails for an utterence, write a line with audio_id and empty recogntion result like this:
  ```
  SPEECHIO_ASR_ZH00001__U_00003  
  ```
* You can try to run and debug your SBI implementation inside your model-image dir, to decode an audio list on your local machine.  Once you can get expected recognition results, then you are ready to go. You don't need to worry about text normalization(upper/lowercase, punctuations, numbers, years etc), WER/CER calculation etc.

---

### 1.5 Runtime Resources
Runtime resources refers to *model files*, *configs*, *cloud-api credentials* etc. These resources can be freely organized by submitters, as long as they are **inside model-image**. We strongly suggest that submitter put all runtime resources into `<model-image>/assets/` directory.  **SBI** code can reach them by using relative path:

For example:
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

then inside SBI code, SBI can always use `./assets/asr.{mdl,cfg}` to locate runtime resources.

---

### 1.6 Sample model-image

* a sample model-image of Cloud-API ASR system:

  https://github.com/speechio/leaderboard/tree/master/models/aispeech_api_zh

* a sample model-image of local ASR system in Kaldi framework:

  https://github.com/speechio/leaderboard/tree/master/models/sample_kaldi_model

---
### 1.7 Validate prepared model-image with leaderboard pipeline on your local machine
1. make sure you can find `MINI` in your local testset-zoo, i.e. `leaderboard/datasets/MINI`
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
      - MINI
    ```
4. run a MINI benchmark:
    ```
    # run this in leaderboard repo
    ops/leaderboard_runner requests/mini.yaml
    ```

5. you can check `leaderboard/results/...<your_model_id>.../{RESULTS,DETAILS}.txt`

If you can pass above local validation, then congratulations, you have successfully made your ASR system reproducible, it's now safe to share and publish.

---

## Step 2: Submit your model-image
2.1 Install aliyun object-storage-service client (one-time-only installation)
```
# run this in leaderboard repo
utils/install_aliyun_oss_client.sh
```

2.2 Move prepared model-image dir into local model-zoo
```
mv <prepared_model_image> leaderboard/models/<model_id>
```
This should have been done already if you did local validation.

2.3 Register your model-image at the end of `leaderboard/models/zoo.yaml`:
```
speechio_kaldi_multicn:
  url: oss://speechio-leaderboard/models/speechio_kaldi_multicn/
wenet_multi_cn:
  url: oss://speechio-leaderboard/models/wenet_multi_cn/
...
...
...
<model_id>:
  url: oss://speechio-leaderboard/models/<model_id>/
```

2.4 Upload your model-image to leaderboard model-zoo
```
ops/push model <model_id>
```
This will upload prepared model-image from your local model-zoo to cloud model-zoo, so that SpeechIO/others can download/reproduce.
And you can always re-run above `ops/push` command to update your model-image in the cloud.

**Notes**: *Unlike large-scale submission for local engines via ops/push, API Model-images are normally small, you can commit API model-images to this github repo via pull request.*

---

## Step 3: Send a benchmark request via a pull request to leaderboard repo
Once you have your model submitted, you can open a PR to this github repo, which adds a request file to `requests` directory:

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
