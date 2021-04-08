# How to submit your model to SpeechIO leaderboard
## overall benchmarking pipeline
![image](misc/leaderboard_design.png)

## Step 1. Prepare your submission
Conceptually, for leaderboard to re-produce and benchmark your ASR system, you need to provide at least 3 things:
* your system dependencies(operation system, software packages)
* ASR resources (e.g. model, config)
* an ASR program that can recognize audio files

In practice, leaderboard requires you to submit a `model directory`, containing:
```
leaderboard@ubuntu: tree ./sample_model_submission_directory

sample_submission_directory
├── docker
│   └── Dockerfile
├── model.yaml
├── README.md
└── SBI
```
this is a contract between submitters and leaderboard, submitters should follow above file structure and file names, now let's explain this contract one by one.

### 1.1 `docker/Dockerfile`
Dockerfile is used to specify your ASR dependencies.  Submitter need to guarentee the Dockerfile properly setup all necessary dependencies of your ASR system.

Besides your dependencies, leaderboard pipeline depends on **`Python3`**. So submitters need to add python3 in Dockerfile, python3 don't need to be default python. Your ASR system can depend on python2/3, and leaderboard pipeline related codes alway have a shebang of `#!/usr/bin/env python3` explicitly.

A sample docker file for commercial clould ASR API call is shown below:
```
FROM ubuntu:20.04
LABEL maintainer="xxx@gmail.com"

RUN apt-get update && apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        python3 && \
    rm -rf /var/lib/apt/lists/*
...
...
``` 
basically it specifies a system build upon ubuntu 20.04 and requires curl to sent http request to clould ASR API.

For submitters who want to benchmark their local system, they need to provide their Dockerfile to install various ML frameworks(such as TensorFlow, PyTorch, Kaldi, Espnet etc).Leaderboard can't help you to write your Dockerfile, we might provide some sample Dockerfiles with common ASR frameworks though.

### 1.2 `model.yaml`
This config list required properties of your ASR system, example below:
```
date: 2021-04-05
task: ASR
language: zh
sample_rate: 16000
author: Jiayu
entity: SpeechIO
email: jerry.jiayu.du@gmail.com
```

* `date`: submission date of this model
* `task`: support `ASR` only
* `language`: language of your ASR model, conforms to `ISO 639-1` language code, lowercase letters.
* `sample_rate`: sample rate of your ASR system. typically 8000(telephone) or 16000(other)
* `author`: submitter
* `entity`: submitter's entity
* `email`: sumitter's contact

leaderboard need these infos to maintain the submitted models in model-zoo

### 1.3 `README.md`
This markdown is optional, but we strongly suggest you provide more infomation about your model, such as:
* number of parameters
* amount of training data
* training framework
* model structures & topology
* objective function
* optimizater
* front end feature type
* ...

recording these info is not only a good memo for submitter himself, but also a good way to help the community to share knowledge.

### 1.4 `model resources`
leaderboard doesn't put any constraint on how submitter organize ASR resources, as long as these resources are **inside model dir**.

`SBI`(the recognizer) is supposed to know where and how to read their resources properly, and for example:
```
leaderboard@ubuntu: tree ./sample_model_directory

sample_model_directory
├── assets
    ├── asr.mdl
    ├── asr.cfg
    ...
...
└── SBI
```

then inside SBI code, SBI can always use `./assets/asr.{mdl,cfg}` to locate those resources.

### 1.5 `SBI`
`SBI` is a submitter implemented program that can decode audio files:
* `SBI` is an executable, could be shebanged `bash`, `python`, `perl` script, or `C/C++ binary`
* `SBI` will be invoked in submitted model dir, so SBI can use relative path to refer to other programs, scripts and shared libraries inside model dir.
* `SBI` performs speech recognition to a list of audios
  ```
  ./SBI <input_audio_list> <result_dir>
  ```

* `input_audio_list` specifies a test set containing short utterances(less than 30 secs), all in standard 16k16bit-mono wav format. Line format and example:
  ```
  SPEECHIO_ASR_ZH00001__U_00001 /home/dataset/SPEECHIO_ASR_ZH00001/U_00001.wav
  SPEECHIO_ASR_ZH00001__U_00002 /home/dataset/SPEECHIO_ASR_ZH00001/U_00002.wav
  ...
  ...
  ```

* `SBI` can write/read arbitrary temporary files in <result_dir>, but final results need to be written to **`<result_dir>/raw_rec.txt`** with **`ASCII/UTF-8`** encoding, with format below:
  ```
  SPEECHIO_ASR_ZH00001__U_00001 I just watched the movie "The Pursuit of Happiness"
  SPEECHIO_ASR_ZH00001__U_00002 rock and roll like a rolling stone
  ...
  ...
  ```

* if recognition fails for an utterence, write a line with audio_uuid and empty recogntion result like this:
  ```
  SPEECHIO_ASR_ZH00001__U_00003  
  ```
* submitters don't need to worry about text normalization(upper/lowercase, punctuations, numbers, years etc), SpeechIO leaderboard will apply universal text normalization to every submission.

## Sample submissions

* a sample submission of Cloud-API based ASR system:

  https://github.com/speechio/leaderboard/tree/master/models/aispeech_api

* a sample submission of local ASR system in Kaldi framework:

  https://github.com/speechio/leaderboard/tree/master/models/sample_kaldi_model
---

## Step 2: Submit your model to SpeechIO Leaderboard
using following command:
```
utils/install_oss.sh # official CLI of aliyun object-storage-service(as Amazon S3), only need to be installed once 
./leaderboard_submit  model_key  ~/work/my_submission_dir_to_speechio_leaderboard
```
**`model_id`** is a unique identifier, used to refer to this model in future benchmarks.

We let submitters to decide their model id. It should be meaningful and unique, for example:
```
speechio_kaldi_pretrain
alphacep_vosk_en
interspeech_xxx_paper_reproduced
stanford_open_conformer
deepspeech_v1
word2vec_v2
```

---
## Step 3: Send a benchmark request by creating a pull request to this github repo
Once you have your model submitted, you can open a PR to this github repo, which adds a request file to `requests` directory:

**`github.com/speechio/leaderboard/requests/give_a_name_for_your_benchmark_request.yaml`**

a sample request file contains following content:
```
date: 2021-04-05
requester: Jiayu
entity: SpeechIO
email: 
  - xxx@gmail.com
model: aliyun_api
test_set:
  - MINI
  - SPEECHIO_ASR_ZH00000
```
where:
* `date`: benchmark request date
* `model`: model key, specifying which model you want to benchmark
* `test_set`: test set id list, which test sets you want to benchmark with
* `email`: a list of email addresses to receive benchmark results

to lookup model id and test_sets id, refer to section 2 & section 3 [here](README.md)

Once we merge your submission pull request, the leaderboard pipeline will:
* init a docker runner to benchmark requested model with requested test sets
* email results to requester