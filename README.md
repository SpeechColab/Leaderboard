# SpeechIO ASR leaderboard
## 1. What is this leaderboard all about?
The architecture of mainstream Automatic Speech Recognition(ASR) system has been evolving rapidly for years.  People claim SOTA here and there(in research papers, in industrial PR articles).  But no one can actually quantitates "how these SOTA systems perform in real-life scenerios?".  People need an objective and comprehensive benchmark to measure ASR system performance.

That's why SpeechIO leaderboard comes in, with emphasis on:
* comprehensive & biggest-ever test sets:
  - carefully curated by SpeechIO authers, crawled from publicly available sources(Youtube, TV programs, Podcast etc)
  - covering various common acoustic scenarios(AM) and content domains(LM & vocabulary) that are familiar to the public.
  - labels from professional human annotators with great cautions and multi-iterations of quality checks.

* an open benchmarking platform:
  - an objective stand-point
  - aggregate benchmarkings of public commercial ASR APIs by default(e.g. google, aws, baidu, alibaba, tencent, iflytek, etc)
  - a simplest interface to implement for submitters
  - open-source, submitters can expect an apple-to-apple comparison with other submitters(including above big-techs' commercial API)

---
## 2. Test Sets Infomations
### 2.1 Chinese Test Sets

| 编号 ID | 名称 <br> Name |场景 <br> Scenario | 内容领域 <br> Topic Domain | 时长 <br> hours | 难度(1-5) <br> Difficulty  |
| --- | --- | --- | --- | --- | --- |
|SPEECHIO_ASR_ZH00000| 接入调试集 <br> For leaderboard submitter debugging | 视频会议、论坛演讲 <br> video conference & forum speech | 经济、货币、金融 <br> economy, currency, finance | 1.0 | ★★☆ |
|SPEECHIO_ASR_ZH00001| 新闻联播 | 新闻播报 <br> TV News | 时政 <br> news & politics | 9 | ★ |
|SPEECHIO_ASR_ZH00002| 鲁豫有约 | 访谈电视节目 <br> TV interview | 名人工作/生活 <br> celebrity & film & music & daily | 3 | ★★☆ |
|SPEECHIO_ASR_ZH00003| 天下足球 | 专题电视节目 <br> TV program | 足球 <br> Sports & Football & Worldcup | 2.7 | ★★☆ |
|SPEECHIO_ASR_ZH00004| 罗振宇跨年演讲 | 会场演讲 <br> Stadium Public Speech | 社会、人文、商业 <br> Society & Culture & Business Trend | 2.7 | ★★ |
|SPEECHIO_ASR_ZH00005| 李永乐老师在线讲堂 | 在线教育 <br> Online Education | 科普 <br> Popular Science | 4.4 | ★★★ |
|SPEECHIO_ASR_ZH00006| 张大仙 & 骚白 王者荣耀直播 | 直播 <br> Live Broadcasting | 游戏 <br> Game | 1.6 | ★★★☆ |
|SPEECHIO_ASR_ZH00007| 李佳琪 & 薇娅 直播带货 | 直播 <br> Live Broadcasting | 电商、美妆 <br> Makeup & Online shopping/advertising | 0.9 | ★★★★☆ |
|SPEECHIO_ASR_ZH00008| 老罗语录 | 线下培训 <br> Offline lecture | 段子、做人 <br> Life & Purpose & Ethics | 1.3 | ★★★★☆ |
|SPEECHIO_ASR_ZH00009| 故事FM | 播客 <br> Podcast | 人生故事、见闻 <br> Ordinary Life Story Telling | 4.5 | ★★☆ |
|SPEECHIO_ASR_ZH00010| 创业内幕 | 播客 <br> Podcast | 创业、产品、投资 <br> Startup & Enterprenuer & Product & Investment | 4.2 | ★★☆ |
|SPEECHIO_ASR_ZH00011| 罗翔 刑法法考培训讲座 | 在线教育 <br> Online Education | 法律 法考 <br> Law & Lawyer Qualification Exams | 3.4 | ★★☆ |
|SPEECHIO_ASR_ZH00012| 张雪峰 考研线上小讲堂 | 在线教育 <br> Online Education | 考研 高校报考 <br> University & Graduate School Entrance Exams | 3.4 | ★★★☆ |
|SPEECHIO_ASR_ZH00013| 谷阿莫&牛叔说电影 | 短视频 <br> VLog | 电影剪辑 <br> Movie Cuts | 1.8 | ★★★ |
|SPEECHIO_ASR_ZH00014| 贫穷料理 & 琼斯爱生活 | 短视频 <br> VLog | 美食、烹饪 <br> Food & Cooking & Gourmet | 1 | ★★★☆ |
|SPEECHIO_ASR_ZH00015| 单田芳 白眉大侠 | 评书 <br> Traditional Podcast | 江湖、武侠 <br> Kongfu Fiction | 2.2 | ★★☆ |
|SPEECHIO_ASR_ZH00016| 德云社相声演出 | 剧场相声 <br> Theater Crosstalk Show | 包袱段子 <br> Funny Stories | 1 | ★★★ |
|SPEECHIO_ASR_ZH00017| 吐槽大会 | 脱口秀电视节目 <br> Standup Comedy | 明星糗事 <br> Celebrity Jokes | 1.8 | ★★☆ |
|SPEECHIO_ASR_ZH00018| 小猪佩奇 & 熊触摸 | 少儿动画 <br> Children Cartoon | 童话故事、日常 <br> Fairy Tale | 0.9 | ★☆ |
|SPEECHIO_ASR_ZH00019| CCTV5 NBA 比赛转播 | 体育赛事解说 <br> Sports Game Live | 篮球、NBA <br> NBA Game | 0.7 | ★★★ |
|SPEECHIO_ASR_ZH00020| 篮球人物 | 纪录片 <br> Documentary | 篮球明星、成长 <br> SNBA Super Stars' Life & History | 2.2 | ★★ |

### 2.2 English Leaderboard
  * TBD
  
---
## 3. Latest Leaderboard result
* Last update: 2021.Jan

  ![result](misc/SpeechIO_TIOBE_2021_01.png)

---


## 4. Prepare your submission

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

### 4.1 docker/Dockerfile
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

### 4.2 model.yaml
This config specifies crucial property of your ASR system, example below:
```
date: 2021-04-05
task: ASR
language: zh
sample_rate: 16000
author: Jiayu
entity: SpeechIO
email: jerry.jiayu.du@gmail.com
```
`date`: submission date of this model
`task`: only `ASR` for now
`language`: language of your ASR model, conforms to `ISO 639-1` language code, lowercase letters.
`sample_rate`: sample rate of your ASR system. typically 8000(telephone) or 16000(other)
`author`: submitter
`entity`: submitter's entity
`email`: sumitter's contact

leaderboard need these infos to maintain the submitted models in model-zoo

### 4.3 README.md
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

### 4.4 model resources
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

### 4.5 SBI program
`SBI` is a submitter implemented program that can decode audio files:
* `SBI` is an executable(`shebang bash/python/perl script`, `C/C++ binary`)
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

---

## 5 upload your model leaderboard model-zoo
using following command:
```
utils/install_oss.sh # this is official CLI of aliyun object-storage-service(as Amazon S3)
./leaderboard_submit  submission_model_uuid   ~/work/my_submission_dir_to_speechio_leaderboard
```
`submission_model_uuid` is a unique identifier for your model, leaderboard let submitters to decide their model uuid.  Generally they should be meaningful, and should not collide with other models. sample submission_uuid
```
speechio_kaldi_baseline_20210401
xxx_ailab_interspeech_xxx_paper_reproduce
```


---
### Step 3: create a benchmarking request
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

Once we merge your submission pull request, the leaderboard pipeline will:
* init a docker runner to benchmark requested model with requested test sets
* email results to requester
