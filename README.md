# SpeechIO ASR leaderboard
## 1. Overview

> "If you can’t measure it, you can’t improve it." -- by *Peter Drucker*

In domain of Automatic Speech Recognition(ASR), people claim SOTA in research papers, in industrial PR articles.  The claim of SOTA is problematic because:
* For industry, there is no objective and quantative benchmark on how these commercial APIs perform in real-life scenarios, at least in public domain.
* For academia, it is becoming harder today to compare ASR models due to the fragmentation of deep learning frameworks and speech toolkits.
* How are academic SOTA and industrial SOTA related ?
---

![Overview](misc/overview.png)
As above figure shows, SpeechIO leaderboard serves as an ASR benchmarking platform, by providing 3 components:

1. TestSet Zoo:
  - SpeechIO test sets: carefully curated by SpeechIO authors, crawled from publicly available sources(Youtube, TV programs, Podcast etc), covering various common acoustic scenarios(AM) and content domains(LM & vocabulary) that are familiar to the public, labeled by professional annotators with great cautions.
  - open-sourced test sets: collected from all sorts of open-sourced datasets
  - open for people who are willing to contribute their own test sets

2. Model Zoo
  - aggregates commercial ASR APIs (e.g. google, aws, baidu, alibaba, tencent, iflytek, etc)
  - incorporate well-known open-sourced models
  - open for people who are willing to share/publish their ASR models

3. an open benchmarking pipeline:
  - defines a simplest-possible contract on the format of test sets, recognition result etc.
  - defines a simplest-possible benchmarking interface for model submitters
  - a fully automated pipeline to perform `prepare` -> `recognize` -> `process` -> `evaluate`, leaderboard users don't need to write code.

With SpeechIO leaderboard, anyone can benchmark/reproduce/compare performances with arbitrary combinations between test-set zoo and model zoo, by simply filling a request form [example form](requests/sample_request.yaml)

---

## 2. TestSet Zoo
<details><summary> Test Sets from Open-Sourced Dataset (ZH) </summary><p>

| 编号 <br> TEST_SET_ID | 说明 <br> DESCRIPTION |
| --- | --- |
| AISHELL-1_TEST | test set of AISHELL-1 |
| AISHELL-2_IOS_TEST | test set of AISHELL-2 (iOS channel) |
| AISHELL-2_ANDROID_TEST | test set of AISHELL-2 (Android channel) |
| AISHELL-2_MIC_TEST | test set of AISHELL-2 (Microphone channel) |

</p></details>

<details><summary> SpeechIO Test Sets (ZH) </summary><p>

| 编号 <br> TEST_SET_ID | 名称 <br> Name |场景 <br> Scenario | 内容领域 <br> Topic Domain | 时长 <br> hours | 难度(1-5) <br> Difficulty  |
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
|SPEECHIO_ASR_ZH00018| 小猪佩奇 & 熊出没 | 少儿动画 <br> Children Cartoon | 童话故事、日常 <br> Fairy Tale | 0.9 | ★☆ |
|SPEECHIO_ASR_ZH00019| CCTV5 NBA 比赛转播 | 体育赛事解说 <br> Sports Game Live | 篮球、NBA <br> NBA Game | 0.7 | ★★★ |
|SPEECHIO_ASR_ZH00020| 篮球人物 | 纪录片 <br> Documentary | 篮球明星、成长 <br> NBA Super Stars' Life & History | 2.2 | ★★ |
|SPEECHIO_ASR_ZH00021| 汽车之家 车辆评测 | 短视频 <br> VLog | 汽车测评 <br> Car benchmarks, Road driving test | 1.7 | ★★★☆ |
|SPEECHIO_ASR_ZH00022| 小艾大叔 豪宅带看 | 短视频 <br> VLog | 房地产、豪宅 <br> Realestate, Mansion tour | 1.7 | ★★★ |
|SPEECHIO_ASR_ZH00023| 无聊开箱 & Zealer评测 | 短视频 <br> VLog | 产品开箱评测 <br> Unboxing | 2 | ★★★ |
|SPEECHIO_ASR_ZH00024| 付老师种植技术 | 短视频 <br> VLog | 农业、种植 <br> Agriculture, Planting | 2.7 | ★★★☆ |
|SPEECHIO_ASR_ZH00025| 石国鹏讲古希腊哲学 | 线下培训 <br> Offline lecture | 历史，古希腊哲学 <br> History, Greek philosophy | 1.3 | ★★☆ |

</p></details>

---

## 3. Model Zoo
<details><summary> Commercial API (ZH) </summary><p>

| 编号 <br> MODEL_ID | 类型 <br> type | 模型作者/所有人 <br> model author/owner | 简介 <br> description | 链接 <br> url |
| --- | --- | --- | --- | --- |
|aispeech_api | Cloud API |思必驰 <br> AISpeech | 思必驰开放平台 | https://cloud.aispeech.com |
|aliyun_api | Cloud API |阿里巴巴 <br> Alibaba | 阿里云 | https://ai.aliyun.com/nls/asr|
|baidu_pro_api | Cloud API |百度 <br> Baidu | 百度智能云(极速版) | https://cloud.baidu.com/product/speech/asr |
| | Cloud API | 讯飞 <br> IFlyTek | 讯飞开放平台(听写服务) | https://www.xfyun.cn/services/voicedictation |
|microsoft_api | Cloud API |微软 <br> Microsoft |Azure| https://azure.microsoft.com/zh-cn/services/cognitive-services/speech-services/ |
|sogou_api | Cloud API |搜狗 <br> Sogou |AI开放平台| https://ai.sogou.com/product/one_recognition/ |
|tencent_api | Cloud API |腾讯 <br> Tencent |腾讯云| https://cloud.tencent.com/product/asr |
|yitu_api | Cloud API |依图 <br> YituTech |依图语音开放平台| https://speech.yitutech.com |
</p></details>

<details><summary> Open-Sourced Pretrained Models (ZH) </summary><p>

| 编号 <br> MODEL_ID | 类型 <br> type | 模型作者/所有人 <br> model author/owner | 简介 <br> description | 链接 <br> url |
| --- | --- | --- | --- | --- |
|speechio_kaldi_multicn | pretrained ASR model | 那兴宇 <br> Xingyu NA | Kaldi预训练模型 <br> Kaldi pretrained ASR | based on Kaldi recipe https://github.com/kaldi-asr/kaldi/tree/master/egs/multi_cn/s5 |

</p></details>

---

## 4. Benchmarking Pipeline
How to submit your own model and get your model benchmarked ?

Follow submission guideline here [HOW_TO_SUBMIT.md](HOW_TO_SUBMIT.md)

---
## 5. Latest Leaderboard Report
![result](misc/SpeechIO_TIOBE_2021_07.png)

---

## Contacts
Contact leaderboard@speechio.ai if you have further inqueires.
