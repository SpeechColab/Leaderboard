# How to submit your model to SpeechIO leaderboard

## Step 1. Prepare your submission
### overall description
Conceptually, for leaderboard to re-produce and benchmark your ASR system, you need to provide at least 3 things:
* your system dependencies(operation system, software packages)
* ASR resources (e.g. model, config)
* an ASR program that can recognize audio files

In practice, leaderboard requires you to submit a `submission directory`, containing:
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
Dockerfile is used to describe your system dependencies.  Submitter should garentee it contains all environment requirements of your ASR system.
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
leaderboard doesn't put any constraint on how submitter organize their model resources, as long as these resources are **inside submission dir**.

`SBI`(the recognizer) is supposed to know how to read resources properly, and for example:
```
leaderboard@ubuntu: tree ./sample_model_submission_directory

sample_submission_directory
├── model
    ├── asr.mdl
    ├── asr.cfg
    ...
...
└── SBI
```

then inside SBI code, SBI can always use `./model/asr.{mdl,cfg}` to locate those resources.

### 1.5 `SBI`
`SBI` is a submitter implemented program that can decode audio files:
* `SBI` is an executable, could be shebanged `bash`, `python`, `perl` script, or a `C/C++ binary`
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

* MBI can write/read temporary files in <result_dir>
* final results need to be written to `<result_dir>/raw_rec.txt`, in `ASCII/UTF-8 encoded` encoding, with following format:
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

* Cloud-API based submission:
  https://github.com/speechio/leaderboard/tree/master/models/aispeech_api

* local model submission:
  https://github.com/speechio/leaderboard/tree/master/models/sample_kaldi_model
---

## Step 2: Submit your model to leaderboard model-zoo
using following command:
```
utils/install_oss.sh # this is official CLI of aliyun object-storage-service(as Amazon S3)
./leaderboard_submit  model_key   ~/work/my_submission_dir_to_speechio_leaderboard
```
`model_key` is a unique identifier for your model, leaderboard let submitters to decide their model key.

model key should be meaningful, and should not collide with other models. sample submission_uuid
```
speechio_kaldi_pretrain
alphacep_vosk_cn
interspeech_xxx_paper_reproduced
```

---
## Step 3: Create a benchmarking request pull request to leaderboard github repo
once you have your model uploaded, you can submit a benchmark request by opening a PR to this github repo

your pull request should add a request.yaml to `github.com/speechio/leaderboard/requests/xxx.yaml`

a sample request is as follows:
```
date: 2021-04-05
requester: Jiayu
entity: SpeechIO
email: 
  - xxx@gmail.com
model: aliyun_api
test_sets:
  - MINI
  - SPEECHIO_ASR_ZH00000
```

some important fields here:

`date`: benchmark request date
`model`: which model you want to benchmark
`test_sets`: which test sets you want to benchmark with
`email`: a list of email addresses to receive benchmark results

to lookup model id and test_sets id, refer to section 2 & section 3 [here](README.md)

Once we merge your submission pull request, the leaderboard pipeline will:
* init a docker runner to benchmark requested model with requested test sets
* email results to requester