# SpeechIO ASR leaderboard
## What is this leaderboard all about?
Since the renaissance of Deep Learning, the field of Automatic Speech Recognition(ASR) has fundamentally changed.  Nowadays, people claim SOTA here and there(in research papers, in industrial PR articals).  But no one can actually quantitates "how these SOTA systems perform in real-life scenerios?".  People need an objective and comprehensive *RULER* to measure ASR systems precisely.

That's why SpeechIO leaderboard comes in, with emphasis on:
* comprehensive & biggest-ever test sets:
  - carefully curated by SpeechIO authers, crawled from publicly available sources(say Youtube, TV programs, Podcast etc)
  - covering various common scenarios and content domains that are familiar to the public.
  - and labelled by human annotators with great cautions and multi-iterations of quality checks.
* an open benchmarking platform:
  - a possibly simplest interface for submitters
  - a stable pipeline
  - an objective stand-point
  - open to anyone, to test and compare your models/algorithms with others.
* performances of top companies' ASR APIs & reproduced paper models are added into leaderboard as "SOTA" references. 

---
## Test Sets Infomations
### English Leaderboard
  * TBD
  
### Chinese Leaderboard

| 编号 ID | 场景 Scenario | 内容领域 Topic Domain | 时长 hours | Difficulty 难度(1-5) |
| --- | --- | --- | --- | --- |
|SIO_ASR_CN0001| 新闻播报 TV News |时政 news & politics | 9 | ★ |
|SIO_ASR_CN0002| 访谈电视节目 TV interview | 名人工作/生活 celebrity & film & music & daily | 3 | ★★☆ |
|SIO_ASR_CN0003| 专题电视节目 TV program | 足球 Sports & Football & Worldcup | 2.7 | ★★☆ |
|SIO_ASR_CN0004| 会场演讲 Stadium Public Speech | 社会、人文、商业 Society & Culture & Business Trend | 2.7 | ★★ |
|SIO_ASR_CN0005| 在线教育 Online Education | 科普 Popular Science | 4.4 | ★★★ |
|SIO_ASR_CN0006| 直播 Live Broadcasting | 游戏 Game | 1.6 | ★★★☆ |
|SIO_ASR_CN0007| 直播 Live Broadcasting | 电商、美妆 Advertising | 0.9 | ★★★★☆ |
|SIO_ASR_CN0008| 线下培训 Offline lecture | 段子、做人 Life & Purpose & Ethics | 1.3 | ★★★★☆ |
|SIO_ASR_CN0009| 播客 Podcast | 人生故事、见闻 Ordinary Life Story Telling | 4.5 | ★★☆ |
|SIO_ASR_CN0010| 播客 Podcast | 创业、产品、投资 Startup & Enterprenuer & Product & Investment | 4.2 | ★★☆ |
|SIO_ASR_CN0011| 在线教育 Online Education | 法律 法考 Law & Lawyer Qualification Exams | 3.4 | ★★☆ |
|SIO_ASR_CN0012| 在线教育 Online Education | 考研 高校报考 University & Graduate School Entrance Exams | 3.4 | ★★★☆ |
|SIO_ASR_CN0013| 短视频 VLog | 电影剪辑  Movie Cuts | 1.8 | ★★★ |
|SIO_ASR_CN0014| 短视频 VLog | 美食、烹饪 Food & Cooking & Gourmet | 1 | ★★★☆ |
|SIO_ASR_CN0015| 评书 Traditional Podcast | 江湖、武侠 Kongfu Fiction | 2.2 | ★★☆ |
|SIO_ASR_CN0016| 相声 Theater Crosstalk Show | 包袱段子 Funny Stories | 1 | ★★★ |
|SIO_ASR_CN0017| 脱口秀 Standup Comedy | 明星糗事 Celebrity Jokes | 1.8 | ★★☆ |
|SIO_ASR_CN0018| 少儿动画 Children Cartoon | 童话故事、日常 Fairy Tale | 0.9 | ★☆ |
|SIO_ASR_CN0019| 体育赛事解说 Sports Game Live | 篮球、NBA NBA Game | 0.7 | ★★★ |
|SIO_ASR_CN0020| 纪录片 Documentary | 篮球明星、成长 NBA Super Stars' Life & History | 2.2 | ★★ |
|SIO_ASR_CN0021| 视频会议、论坛演讲 video conference & forum speech | 经济、货币、金融 economy, currency, finance | 1.0 | ★★☆ |

---
## Leaderboard result as of 2021.Jan
  ![result](misc/SpeechIO_TIOBE_2021_01.png)

---


## How to submit your own benchmarking request?
To benmark your ASR system, leaderboard pipeline needs you to provide a self-contained `submission directory`, containing:
* `A program` that performs speech recognition to a list of audios, we call this program "Minimal Benchmarking Interface", MBI for short.
* `A Dockerfile` that prepares runtime envrionment dependencies of your MBI program(e.g. ubuntu, centos, conda, pytorch, tf, kaldi etc)
* `Resources`(models/config files) that are required by your MBI program 

---
### Step 1: implement your Minimal Benchmarking Interface(MBI) program.
```
./MBI <input_audio_list> <result_dir>
```
This is `Minimal Benchmarking Interface(MBI)`, and it's the only concept you need to know to submit your benchmarking request:
* `MBI` is an executable(`shebang bash/python/perl script`, `C/C++ binary`) that performs speech recognition to a list of audios.
* `input_audio_list` specifies a test set containing short utterances(less than 30 secs), all in standard 16k16bit-mono wav format. Line format and example:
  ```
  <audio_uuid> <audio_path>
  ```


  ```
  TST_00001__U_00001 /home/dataset/SIO_ASR_CN0001/U_00001.wav
  TST_00001__U_00002 /home/dataset/SIO_ASR_CN0001/U_00002.wav
  ...
  ...
  ...
  ```

* MBI can write/read temporary files in <result_dir>, but final results need to be dumped into `<result_dir>/raw_rec.txt` with format:
  ```
  <audio_uuid> <speech_recognition_result>
  ```
  ```
  SIO_ASR_CN0001__U_00001 I just watched the movie "The Pursuit of Happiness"
  ...
  ...
  ...
  ```

* `<result_dir>/raw_rec.txt` needs to be `ASCII/UTF-8 encoded`.
* For each line, the first field is audio's uuid, followed by a `tab` or `space`, and the rest of the line is recognition result.
* if recognition fails for an utterence, write a line with audio_uuid and empty recogntion result like this:
  ```
  SIO_ASR_CN0001__U_00002  
  ```
* submitters don't need to worry about text normalization(upper/lowercase, punctuations, numbers, years etc), SpeechIO leaderboard will apply universal text normalization to every submission.

---
### Step 2: prepare and upload your submission directory to leaderboard model hub
This directory should have:
* `MBI`: MBI program
* `docker/Dockerfile`: dockerfile that setups all dependencies of your MBI program. 
* all necessary resources of your MBI program(such as models, configs...), you can name and organize these resources whatever you like as long as they are inside your submission directory. Your MBI program read these, leaderboard pipeline doesn't care.

for example, in a sample submission dir, `tree .` gives:
```
├── MBI
├── assets
│   ├── HCLG.fst
│   ├── conf
│   │   └── fbank_hires.conf
│   ├── final.mdl
│   └── words.txt
└── docker
    └── Dockerfile
```

---
### Step 3: create a pull request for your submission
we accept a submission by merging a pull request from you to our github repo.

your pull request should add a submission yaml as following:
```
github.com/speechio/leaderboard/submissions/{your_submission_key}/info.yml
```

currently, we let you define your own `submission key`.
a sample submission can be found [here](https://github.com/speechio/leaderboard/tree/master/submissions/kaldi_baseline/info.yml) as followings:
```
--- # SpeechIO Leaderboard Submission
key: kaldi_baseline
task: ASR
date: 2021-01-01
entity: SpeechIO
author: Jerry
email: kkk@gmail.com
url: oss://speechio-leaderboard/hub/kaldi_baseline
test_sets:
  - SIO_ASR_CN0001
  - SIO_ASR_CN0015
model:
  params: 40M
  front_end: FBank(dim=80) + specaug
  descripton: CNN + TDNN-F
  components:
    - conv: 1 layer of dim 256
    - tdnn: 15 layers of 2048-dim with 256-dim bottleneck
  objective_function: LF-MMI
  optimizer: NG-SGD
  open_source: True

```
some important fields here:
* `url`: point to the location of your submission directory
* `test_sets`: containing the test sets that you want to benchmark with

## How long to wait for benchmarking results?
Once we merge your submission pull request, the leaderboard pipeline will:
* download your submission directory from leaderboard model hub
* build a docker image according to your Dockerfile
* start a container instance, use your MBI program to iterate over `test_sets` section one by one in your submission request
* post processing all your results(word/char segmentation, text normalization) and calculate WER/CER

## Where to get benchmarking results?
TBD website? github repo?
