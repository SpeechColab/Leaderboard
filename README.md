# SpeechIO ASR leaderboard
## 1. Overview

> "If you can’t measure it, you can’t improve it." -- *Peter Drucker*

Regarding to the field of Automatic Speech Recognition(ASR) today, people often claim their systems to be SOTA, in research papers, in industrial PR articles etc.  The claim of SOTA is not as informative as one might expect, because:
* For industry, there is no objective and quantative benchmark on how these commercial APIs perform in real-life scenarios, at least in public domain.
* For academia, it is becoming harder today to compare ASR models due to the fragmentation of research toolkits and ecosystem.
* How are academic SOTA and industrial SOTA related ?

---

![Overview](misc/overview.png)

As above figure shows, SpeechIO leaderboard serves as an ASR benchmarking platform, by providing 3 components:

1. TestSet Zoo: A collection of test sets covering wide range of speech recognition scenarios
2. Model Zoo: A collection of models including commercial APIs and open-sourced pretrained models
3. An automated benchmarking pipeline:
   - defines a simplest-possible specification on recognition interface, the format of input test sets, the format of output recognition results.
   - As long as model submitters conform to this specification, a fully automated pipeline will take care of the rest (e.g. data preparation -> recognition invocation -> text post processing -> WER/CER/SER evaluation)

With SpeechIO leaderboard, anyone can benchmark/reproduce/compare performances with arbitrary combinations between test-set zoo and model zoo, by simply filling a request form [example form](requests/sample_request.yaml)

---

## 2. TestSet Zoo

To pull a released test set:
```
ops/pull dataset <TEST_SET_ID>
```

<details><summary> Public Test Sets (EN & ZH) </summary><p>

| 已公开 <br> Released | 编号 <br> TEST_SET_ID | 说明 <br> DESCRIPTION | 语言 <br> LANGUAGE |
| --- | --- | --- | --- |
| &check; | LIBRISPEECH_TEST_CLEAN | "test_clean" set of LibriSpeech | en |
| &check; | LIBRISPEECH_TEST_OTHER | "test_other" set of LibriSpeech | en |
| &check; | AISHELL1_TEST | test set of AISHELL-1 | zh |
| &check; | AISHELL2_IOS_TEST | test set of AISHELL-2 (iOS channel) | zh |
| &check; | AISHELL2_ANDROID_TEST | test set of AISHELL-2 (Android channel) | zh |
| &check; | AISHELL2_MIC_TEST | test set of AISHELL-2 (Microphone channel) | zh |

</p></details>

<details><summary> SpeechIO Test Sets (ZH) </summary><p>

SpeechIO test sets are carefully curated by SpeechIO authors, crawled from publicly available sources (Youtube, TV programs, Podcast etc), covering various well-known acoustic scenarios(AM) and content domains(LM & vocabulary), labeled by professional annotators.

| 已公开 <br> Released | 编号 <br> TEST_SET_ID | 名称 <br> Name |场景 <br> Scenario | 内容领域 <br> Topic Domain | 时长 <br> hours | 难度(1-5) <br> Difficulty  |
| --- | --- | --- | --- | --- | --- | --- |
| &check; |SPEECHIO_ASR_ZH00000| 接入调试集 <br> For leaderboard submitter debugging | 视频会议、论坛演讲 <br> video conference & forum speech | 经济、货币、金融 <br> economy, currency, finance | 1.0 | ★★☆ |
| &check; |SPEECHIO_ASR_ZH00001| 新闻联播 | 新闻播报 <br> TV News | 时政 <br> news & politics | 9 | ★ |
| &cross; |SPEECHIO_ASR_ZH00002| 鲁豫有约 | 访谈电视节目 <br> TV interview | 名人工作/生活 <br> celebrity & film & music & daily | 3 | ★★☆ |
| &cross; |SPEECHIO_ASR_ZH00003| 天下足球 | 专题电视节目 <br> TV program | 足球 <br> Sports & Football & Worldcup | 2.7 | ★★☆ |
| &cross; |SPEECHIO_ASR_ZH00004| 罗振宇跨年演讲 | 会场演讲 <br> Stadium Public Speech | 社会、人文、商业 <br> Society & Culture & Business Trend | 2.7 | ★★ |
| &cross; |SPEECHIO_ASR_ZH00005| 李永乐老师在线讲堂 | 在线教育 <br> Online Education | 科普 <br> Popular Science | 4.4 | ★★★ |
| &cross; |SPEECHIO_ASR_ZH00006| 张大仙 & 骚白 王者荣耀直播 | 直播 <br> Live Broadcasting | 游戏 <br> Game | 1.6 | ★★★☆ |
| &cross; |SPEECHIO_ASR_ZH00007| 李佳琪 & 薇娅 直播带货 | 直播 <br> Live Broadcasting | 电商、美妆 <br> Makeup & Online shopping/advertising | 0.9 | ★★★★☆ |
| &cross; |SPEECHIO_ASR_ZH00008| 老罗语录 | 线下培训 <br> Offline lecture | 段子、做人 <br> Life & Purpose & Ethics | 1.3 | ★★★★☆ |
| &cross; |SPEECHIO_ASR_ZH00009| 故事FM | 播客 <br> Podcast | 人生故事、见闻 <br> Ordinary Life Story Telling | 4.5 | ★★☆ |
| &cross; |SPEECHIO_ASR_ZH00010| 创业内幕 | 播客 <br> Podcast | 创业、产品、投资 <br> Startup & Enterprenuer & Product & Investment | 4.2 | ★★☆ |
| &cross; |SPEECHIO_ASR_ZH00011| 罗翔 刑法法考培训讲座 | 在线教育 <br> Online Education | 法律 法考 <br> Law & Lawyer Qualification Exams | 3.4 | ★★☆ |
| &cross; |SPEECHIO_ASR_ZH00012| 张雪峰 考研线上小讲堂 | 在线教育 <br> Online Education | 考研 高校报考 <br> University & Graduate School Entrance Exams | 3.4 | ★★★☆ |
| &cross; |SPEECHIO_ASR_ZH00013| 谷阿莫&牛叔说电影 | 短视频 <br> VLog | 电影剪辑 <br> Movie Cuts | 1.8 | ★★★ |
| &cross; |SPEECHIO_ASR_ZH00014| 贫穷料理 & 琼斯爱生活 | 短视频 <br> VLog | 美食、烹饪 <br> Food & Cooking & Gourmet | 1 | ★★★☆ |
| &cross; |SPEECHIO_ASR_ZH00015| 单田芳 白眉大侠 | 评书 <br> Traditional Podcast | 江湖、武侠 <br> Kongfu Fiction | 2.2 | ★★☆ |
| &cross; |SPEECHIO_ASR_ZH00016| 德云社相声演出 | 剧场相声 <br> Theater Crosstalk Show | 包袱段子 <br> Funny Stories | 1 | ★★★ |
| &cross; |SPEECHIO_ASR_ZH00017| 吐槽大会 | 脱口秀电视节目 <br> Standup Comedy | 明星糗事 <br> Celebrity Jokes | 1.8 | ★★☆ |
| &cross; |SPEECHIO_ASR_ZH00018| 小猪佩奇 & 熊出没 | 少儿动画 <br> Children Cartoon | 童话故事、日常 <br> Fairy Tale | 0.9 | ★☆ |
| &cross; |SPEECHIO_ASR_ZH00019| CCTV5 NBA 比赛转播 | 体育赛事解说 <br> Sports Game Live | 篮球、NBA <br> NBA Game | 0.7 | ★★★ |
| &cross; |SPEECHIO_ASR_ZH00020| 篮球人物 | 纪录片 <br> Documentary | 篮球明星、成长 <br> NBA Super Stars' Life & History | 2.2 | ★★ |
| &cross; |SPEECHIO_ASR_ZH00021| 汽车之家 车辆评测 | 短视频 <br> VLog | 汽车测评 <br> Car benchmarks, Road driving test | 1.7 | ★★★☆ |
| &cross; |SPEECHIO_ASR_ZH00022| 小艾大叔 豪宅带看 | 短视频 <br> VLog | 房地产、豪宅 <br> Realestate, Mansion tour | 1.7 | ★★★ |
| &cross; |SPEECHIO_ASR_ZH00023| 无聊开箱 & Zealer评测 | 短视频 <br> VLog | 产品开箱评测 <br> Unboxing | 2 | ★★★ |
| &cross; |SPEECHIO_ASR_ZH00024| 付老师种植技术 | 短视频 <br> VLog | 农业、种植 <br> Agriculture, Planting | 2.7 | ★★★☆ |
| &cross; |SPEECHIO_ASR_ZH00025| 石国鹏讲古希腊哲学 | 线下培训 <br> Offline lecture | 历史，古希腊哲学 <br> History, Greek philosophy | 1.3 | ★★☆ |

</p></details>

---

## 3. Model Zoo

To pull a released model:
```
ops/pull model <MODEL_ID>
```

<details><summary> Commercial API (EN) </summary><p>

| 已公开 <br> Released | 编号 <br> MODEL_ID | 类型 <br> type | 模型作者/所有人 <br> model author/owner | 简介 <br> description | 链接 <br> url |
| --- | --- | --- | --- | --- | --- |
| &check; | [aliyun_api_en](models/aispeech_api_en/) | Cloud API | 阿里云 <br> Alibaba Cloud | 阿里云智能语音交互 | https://www.alibabacloud.com/product/intelligent-speech-interaction |
| &check; | [google_api_en](models/google_api_en/) | Cloud API | 谷歌 <br> Google Cloud Speech API | 谷歌云平台语音识别 | https://cloud.google.com/speech-to-text |
| &check; | [microsoft_api_en](models/microsoft_api_en/) | Cloud API |微软 <br> Microsoft | Azure认知服务 | https://azure.microsoft.com/en-us/services/cognitive-services/speech-to-text/ |

</p></details>

<details><summary> Commercial API (ZH) </summary><p>

| 已公开 <br> Released | 编号 <br> MODEL_ID | 类型 <br> type | 模型作者/所有人 <br> model author/owner | 简介 <br> description | 链接 <br> url |
| --- | --- | --- | --- | --- | --- |
| &check; | [aispeech_api_zh](models/aispeech_api_zh/) | Cloud API |思必驰 <br> AISpeech | 思必驰开放平台 | https://cloud.aispeech.com |
| &check; | [aliyun_api_zh](models/aliyun_api_zh/) | Cloud API |阿里巴巴 <br> Alibaba | 阿里云 | https://ai.aliyun.com/nls/asr|
| &check; | [baidu_pro_api_zh](models/baidu_pro_api_zh/) | Cloud API |百度 <br> Baidu | 百度智能云(极速版) | https://cloud.baidu.com/product/speech/asr |
| &cross; | | Cloud API | 讯飞 <br> IFlyTek | 讯飞开放平台(听写服务) | https://www.xfyun.cn/services/voicedictation |
| &check; | [iflytek_lfasr_api_zh](models/iflytek_lfasr_api_zh/) | Cloud API | 讯飞 <br> IFlyTek | 讯飞开放平台(转写服务) | https://www.xfyun.cn/services/lfasr |
| &check; | [microsoft_api_zh](models/microsoft_api_zh/) | Cloud API |微软 <br> Microsoft |Azure| https://azure.microsoft.com/zh-cn/services/cognitive-services/speech-services/ |
| &check; | [sogou_api_zh](models/sogou_api_zh/) | Cloud API |搜狗 <br> Sogou |AI开放平台| https://ai.sogou.com/product/one_recognition/ |
| &check; | [tencent_api_zh](models/tencent_api_zh/) | Cloud API |腾讯 <br> Tencent |腾讯云| https://cloud.tencent.com/product/asr |
| &check; | [yitu_api_zh](models/yitu_api_zh/) | Cloud API |依图 <br> YituTech |依图语音开放平台| https://speech.yitutech.com |

</p></details>

<details><summary> Open-Sourced Pretrained Models (ZH) </summary><p>

| 已公开 <br> Released | 编号 <br> MODEL_ID | 类型 <br> type | 模型作者/所有人 <br> model author/owner | 简介 <br> description | 链接 <br> url |
| --- | --- | --- | --- | --- | --- |
| &check; | speechio_kaldi_multicn | pretrained ASR model | 那兴宇 <br> Xingyu NA | Kaldi预训练模型 <br> Kaldi pretrained ASR | based on Kaldi recipe https://github.com/kaldi-asr/kaldi/tree/master/egs/multi_cn/s5 |
| &check; | wenet_multi_cn | pretrained ASR model | Binbin Zhang@<br> [wenet-e2e](https://github.com/wenet-e2e/) | WeNet pretrained model on mulit_cn dataset  | WeNet multi_cn recipe https://github.com/wenet-e2e/wenet/tree/main/examples/multi_cn/s0 |

</p></details>

---

## 4. Benchmarking Pipeline Specification
To submit your own model and get it benchmarked, please follow benchmarking pipeline specification here: [HOW_TO_SUBMIT](HOW_TO_SUBMIT.md)

---
## 5. Latest Leaderboard Report
![result](misc/SpeechIO_TIOBE_2021_07.png)

---

## Contacts
Email: leaderboard@speechio.ai
