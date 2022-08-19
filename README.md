# SpeechColab ASR leaderboard
## 1. Overview

> "If you can’t measure it, you can’t improve it." -- *Peter Drucker*

SpeechIO leaderboard serves as an ASR benchmarking platform by providing 3 components:

1. **TestSet Zoo**: A collection of test sets covering wide range of speech recognition tasks & scenarios

2. **Model Zoo**: A collection of models including commercial APIs & open-sourced models

3. **Benchmarking Pipeline**: a simple & well-specified pipeline to take care of data preparation / recognition / post processing / error rate evaluation.

With SpeechIO leaderboard, _**anyone should be able to benchmark, reproduce, compare all these ASR systems locally**_

![Overview](misc/overview.png)
---

## 2. TestSet Zoo

### Academic Test Sets

| 已公开 <br> UNLOCKED | 编号 <br> TEST_SET_ID | 说明 <br> DESCRIPTION | 语言 <br> LANGUAGE |
| --- | --- | --- | --- |
| &check; | AISHELL1_TEST | test set of AISHELL-1 | zh |
| &check; | AISHELL2_IOS_TEST | test set of AISHELL-2 (iOS channel) | zh |
| &check; | AISHELL2_ANDROID_TEST | test set of AISHELL-2 (Android channel) | zh |
| &check; | AISHELL2_MIC_TEST | test set of AISHELL-2 (Microphone channel) | zh |
| &check; | LIBRISPEECH_TEST_CLEAN | "test_clean" set of [LibriSpeech](https://www.openslr.org/12) | en |
| &check; | LIBRISPEECH_TEST_OTHER | "test_other" set of [LibriSpeech](https://www.openslr.org/12) | en |
| &check; | GIGASPEECH_V1.0.0_DEV | dev set of [GigaSpeech](https://github.com/SpeechColab/GigaSpeech) | en |
| &check; | GIGASPEECH_V1.0.0_TEST | test set of [GigaSpeech](https://github.com/SpeechColab/GigaSpeech) | en |

### SpeechIO Test Sets

SpeechIO test sets are carefully curated by SpeechIO authors, crawled from publicly available sources (Youtube, TV programs, Podcast etc), covering various well-known acoustic scenarios(AM) and topic domains(LM & vocabulary), labeled by payed professional annotators.

| 已公开 <br> UNLOCKED | 编号 <br> TEST_SET_ID | 名称 <br> NAME | 场景 <br> SCENARIO | 内容领域 <br> TOPIC | 时长 <br> HOURS | 难度(1-5) <br> DIFFICULTY  |
| --- | --- | --- | --- | --- | --- | --- |
| &check; |SPEECHIO_ASR_ZH00000| 调试集 <br> for debugging | 视频会议、论坛演讲 <br> conference & speech | 经济、货币、金融 <br> economy, currency, finance | 1.0 | ★★☆ |
| &check; |SPEECHIO_ASR_ZH00001| 新闻联播 | 新闻播报 <br> TV News | 时政 <br> news & politics | 9 | ★ |
| &check; |SPEECHIO_ASR_ZH00002| 鲁豫有约 | 访谈电视节目 <br> TV interview | 名人工作/生活 <br> celebrity & film & music & daily | 3 | ★★☆ |
| &check; |SPEECHIO_ASR_ZH00003| 天下足球 | 专题电视节目 <br> TV program | 足球 <br> Sports & Football & Worldcup | 2.7 | ★★☆ |
| &check; |SPEECHIO_ASR_ZH00004| 罗振宇跨年演讲 | 会场演讲 <br> Stadium Public Speech | 社会、人文、商业 <br> Society & Culture & Business Trend | 2.7 | ★★ |
| &check; |SPEECHIO_ASR_ZH00005| 李永乐讲堂 | 在线教育 <br> Online Education | 科普 <br> Popular Science | 4.4 | ★★★ |
| &check; |SPEECHIO_ASR_ZH00006| 王者荣耀 <br> 张大仙 & 骚白 | 直播 <br> Live Broadcasting | 游戏 <br> Game | 1.6 | ★★★☆ |
| &check; |SPEECHIO_ASR_ZH00007| 直播带货 <br> 李佳琪 & 薇娅 | 直播 <br> Live Broadcasting | 电商、美妆 <br> Makeup & Online shopping/advertising | 0.9 | ★★★★☆ |
| &check; |SPEECHIO_ASR_ZH00008| 老罗语录 | 线下培训 <br> Offline lecture | 段子、做人 <br> Life & Purpose & Ethics | 1.3 | ★★★★☆ |
| &check; |SPEECHIO_ASR_ZH00009| 故事FM | 播客 <br> Podcast | 人生故事、见闻 <br> Ordinary Life Story Telling | 4.5 | ★★☆ |
| &check; |SPEECHIO_ASR_ZH00010| 创业内幕 | 播客 <br> Podcast | 创业、产品、投资 <br> Startup & Enterprenuer & Product & Investment | 4.2 | ★★☆ |
| &check; |SPEECHIO_ASR_ZH00011| 罗翔刑法法考 | 在线教育 <br> Online Education | 法律 法考 <br> Law & Lawyer Qualification Exams | 3.4 | ★★☆ |
| &check; |SPEECHIO_ASR_ZH00012| 张雪峰考研 | 在线教育 <br> Online Education | 考研 高校报考 <br> University & Graduate School Entrance Exams | 3.4 | ★★★☆ |
| &check; |SPEECHIO_ASR_ZH00013| 谷阿莫 <br> 牛叔说电影 | 短视频 <br> VLog | 电影剪辑 <br> Movie Cuts | 1.8 | ★★★ |
| &check; |SPEECHIO_ASR_ZH00014| 贫穷料理 <br> 琼斯爱生活 | 短视频 <br> VLog | 美食、烹饪 <br> Food & Cooking & Gourmet | 1 | ★★★☆ |
| &check; |SPEECHIO_ASR_ZH00015| 单田芳 白眉大侠 | 评书 <br> Traditional Podcast | 江湖、武侠 <br> Kongfu Fiction | 2.2 | ★★☆ |
| &cross; |SPEECHIO_ASR_ZH00016| 德云社演出 | 剧场相声 <br> Theater Crosstalk Show | 包袱段子 <br> Funny Stories | 1 | ★★★ |
| &cross; |SPEECHIO_ASR_ZH00017| 吐槽大会 | 脱口秀电视节目 <br> Standup Comedy | 明星糗事 <br> Celebrity Jokes | 1.8 | ★★☆ |
| &cross; |SPEECHIO_ASR_ZH00018| 小猪佩奇 <br> 熊出没 | 少儿动画 <br> Children Cartoon | 童话故事、日常 <br> Fairy Tale | 0.9 | ★☆ |
| &cross; |SPEECHIO_ASR_ZH00019| CCTV5 NBA 转播 | 体育赛事解说 <br> Sports Game Live | 篮球、NBA <br> NBA Game | 0.7 | ★★★ |
| &cross; |SPEECHIO_ASR_ZH00020| 篮球人物 | 纪录片 <br> Documentary | 篮球明星、成长 <br> NBA Super Stars' Life & History | 2.2 | ★★ |
| &cross; |SPEECHIO_ASR_ZH00021| 汽车之家评测 | 短视频 <br> VLog | 汽车测评 <br> Car benchmarks, Road driving test | 1.7 | ★★★☆ |
| &cross; |SPEECHIO_ASR_ZH00022| 小艾大叔 豪宅带看 | 短视频 <br> VLog | 房地产、豪宅 <br> Realestate, Mansion tour | 1.7 | ★★★ |
| &cross; |SPEECHIO_ASR_ZH00023| 无聊开箱 <br> Zealer评测 | 短视频 <br> VLog | 产品开箱评测 <br> Unboxing | 2 | ★★★ |
| &cross; |SPEECHIO_ASR_ZH00024| 付老师种植技术 | 短视频 <br> VLog | 农业、种植 <br> Agriculture, Planting | 2.7 | ★★★☆ |
| &cross; |SPEECHIO_ASR_ZH00025| 石国鹏讲历史 | 线下培训 <br> Offline lecture | 历史，古希腊哲学 <br> History, Greek philosophy | 1.3 | ★★☆ |
| &cross; |SPEECHIO_ASR_ZH00026| 张震鬼故事 | 广播节目 <br> Broadcasting Program | 鬼故事 <br> Horror Stories | 2.4 | ★★★ |
| &cross; |SPEECHIO_ASR_ZH00027| 华语辩论世界杯 | 辩论赛 <br> Debates Contest | 兴趣、技能、成长 <br> Hobby, Skill, Growth | 1.4 | ★★★ |
| &cross; |SPEECHIO_ASR_ZH00028| 时政现场同传 | 同声传译 <br> Simultaneous Translation | 时政、社会公共治理 <br> News & Events on Public Governance | 2.1 | ★★★☆ |
| &cross; |SPEECHIO_ASR_ZH00029| 港台明星访谈 <br> 周杰伦,曾志伟 <br> 张家辉,陈小春 <br> 周星驰 | 口音(港台) <br> HongKong/Taiwan Accents | 娱乐、生活、演艺 <br> Entertainment, Acting, Musics | 1.5 | ★★★☆ |
| &cross; |SPEECHIO_ASR_ZH00030| 世界青年说 | 口音(老外) <br> Foreigner Accents | 异国文化比较 <br> Cultural Difference | 2 | ★★★☆ |

### How to get a test set
To download an **unlocked** test set from cloud to your local dir `leaderboard/datasets/<TEST_SET_ID>`:
```
ops/pull dataset <TEST_SET_ID>
```

---

## 3. Model Zoo
There are 2 types of models in model zoo: `cloud API model` & `pretrained model`:

### ZH models 
#### Cloud API Models (ZH)
| 已公开 <br> UNLOCKED | 编号 <br> MODEL_ID | 类型 <br> TYPE | 厂商 <br> PROVIDER | 简介 <br> DESCRIPTION | 链接 <br> URL |
| --- | --- | --- | --- | --- | --- |
| &check; | [aispeech_api_zh](models/aispeech_api_zh/) | Cloud API | 思必驰 <br> AISpeech | 思必驰开放平台 | [official link](https://cloud.aispeech.com) |
| &check; | [aliyun_api_zh](models/aliyun_api_zh/) | Cloud API | 阿里巴巴 <br> Alibaba | 阿里云 - 一句话识别 | [official link](https://ai.aliyun.com/nls/asr) |
| &check; | [aliyun_ftasr_api_zh](models/aliyun_ftasr_api_zh/) | Cloud API | 阿里巴巴 <br> Alibaba | 阿里云 - 文件识别(非流式) | [official link](https://ai.aliyun.com/nls/asr) |
| &check; | [baidu_pro_api_zh](models/baidu_pro_api_zh/) | Cloud API | 百度 <br> Baidu | 百度智能云 <br> (极速版) | [official link](https://cloud.baidu.com/product/speech/asr) |
| &check; | [iflytek_lfasr_api_zh](models/iflytek_lfasr_api_zh/) | Cloud API | 讯飞 <br> IFlyTek | 讯飞开放平台 <br> (转写,非流式) | [official link](https://www.xfyun.cn/services/lfasr) |
| &check; | [microsoft_sdk_zh](models/microsoft_sdk_zh/) | Cloud API | 微软 <br> Microsoft | Azure | [official link](https://azure.microsoft.com/zh-cn/services/cognitive-services/speech-services/) |
| &check; | [tencent_api_zh](models/tencent_api_zh/) | Cloud API | 腾讯 <br> Tencent | 腾讯云 | [official link](https://cloud.tencent.com/product/asr) |
| &check; | [yitu_api_zh](models/yitu_api_zh/) | Cloud API | 依图 <br> YituTech |依图语音开放平台 | [official link](https://speech.yitutech.com) |

#### Pretrained Models (ZH)
| 已公开 <br> UNLOCKED | 编号 <br> MODEL_ID | 类型 <br> TYPE | 作者 <br> AUTHOR | 简介 <br> DESCRIPTION |
| --- | --- | --- | --- | --- |
| &check; | speechio_kaldi_multicn | Pretrained | Xingyu NA(那兴宇) | Kaldi multi_cn [recipe](https://github.com/kaldi-asr/kaldi/tree/master/egs/multi_cn/s5) |
| &check; | wenet_multi_cn | Pretrained | Binbin Zhang(张彬彬)@[wenet-e2e](https://github.com/wenet-e2e/) |  WeNet multi_cn [recipe](https://github.com/wenet-e2e/wenet/tree/main/examples/multi_cn/s0) |
| &check; | vosk_model_cn | Pretrained | [alphacephei](https://alphacephei.com/vosk) | Chinese engine of [Vosk](https://alphacephei.com/vosk/models) |
| &check; | wenet_wenetspeech | Pretrained | Binbin Zhang(张彬彬)@[wenet-e2e](https://github.com/wenet-e2e/) |  WeNet wenetspeech [recipe](https://github.com/wenet-e2e/wenet/tree/main/examples/wenetspeech/s0) |

### EN models
#### Cloud API Models (EN)
| 已公开 <br> UNLOCKED | 编号 <br> MODEL_ID | 类型 <br> TYPE | 厂商 <br> PROVIDER | 简介 <br> DESCRIPTION | 链接 <br> URL |
| --- | --- | --- | --- | --- | --- |
| &check; | [aliyun_api_en](models/aliyun_api_en/) | Cloud API | 阿里巴巴 <br> Alibaba | 阿里云 - 一句话识别 | [official link](https://www.alibabacloud.com/product/intelligent-speech-interaction) |
| &check; | [amazon_api_en](models/amazon_api_en/) | Cloud API | 亚马逊 <br> Amazon | 亚马逊云服务平台 | [official link](https://aws.amazon.com/cn/transcribe/) |
| &check; | [baidu_api_en](models/baidu_api_en/) | Cloud API | 百度 <br> Baidu | 百度智能云 | [official link](https://cloud.baidu.com/product/speech/asr) |
| &check; | [google_api_en](models/google_api_en/) | Cloud API | 谷歌 <br> Google | 谷歌云 | [official link](https://cloud.google.com/speech-to-text) |
| &check; | [microsoft_sdk_en](models/microsoft_sdk_en/) | Cloud API | 微软 <br> Microsoft | Azure | [official link](https://azure.microsoft.com/en-us/services/cognitive-services/speech-to-text/) |
| &check; | [tencent_api_en](models/tencent_api_en/) | Cloud API | 腾讯 <br> Tencent | 腾讯云 | [official link](https://cloud.tencent.com/product/asr) |

#### Pretrained Models (EN)
| 已公开 <br> UNLOCKED | 编号 <br> MODEL_ID | 类型 <br> TYPE | 作者 <br> AUTHOR | 简介 <br> DESCRIPTION |
| --- | --- | --- | --- | --- |
| &check; | vosk_model_en | Pretrained | [alphacephei](https://alphacephei.com/vosk) | English engine of [Vosk](https://alphacephei.com/vosk/models) |
| &check; | vosk_model_en_large | Pretrained | [alphacephei](https://alphacephei.com/vosk) | Large English engine of [Vosk](https://alphacephei.com/vosk/models) |
| &check; | deepspeech_model_en | Pretrained | [deepspeech](https://github.com/mozilla/DeepSpeech)| Latest English ASR Model of [deepspeech](https://github.com/mozilla/DeepSpeech/releases/tag/v0.9.3)
| &check; | coqui_model_en | Pretrained | [coqui](https://coqui.ai/) | English engine of [coqui](https://coqui.ai/models)|
| &check; | NeMo_conformer_en | Pretrained | [NeMo](https://github.com/NVIDIA/NeMo) | English engine of [NeMo_conformer](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo/models/stt_en_conformer_ctc_large)|

### How to get a model
* cloud API models are stored in this github repo `Leaderboard/models/*`
* pretrained models are stored in cloud, to download an **unlocked** model to your local dir (i.e. `Leaderboard/models/<MODEL_ID>`):
```
ops/pull model <MODEL_ID>
```

---

## 4. Benchmarking Pipeline
Follow this [specification](HOW_TO_SUBMIT.md) to submit your model and get it benchmarked over all test sets.

With downloaded models & test sets, you can trigger the benchmarking pipeline locally:
```
ops/leaderboard_runner requests/request.yaml
```
Here `request.yaml` specifies a <MODEL_ID> and a list of <TEST_SET_ID> to be tested (see examples in above specification).

---
## 5. Ranking

### Ranking on unlocked test sets only
| Rank排名 | Model模型 | CER字错误率 | Submission date 提交时间 |
| --- | --- | --- | --- | 
| 1 | yitu_api_zh | 2.85 % | 2022.05 |
| 2 | aliyun_api | 3.03% | 2022.05 |
| 3 | microsoft_sdk_zh | 3.04% | 2022.05 |
| 4 | bilibili_api_zh | 3.09% | 2022.06 |
| 5 | aispeech_api_zh | 3.39% | 2022.05 |
| 6 | tencent_api_zh | 3.56% | 2022.05 |
| 7 | iflytek_lfasr_api_zh | 3.69% | 2022.05 |
| 8 | baidu_pro_api_zh | 6.64% | 2022.05 |

### Ranking on all SpeechIO test sets
| Rank排名 | Model模型 | CER字错误率 | Submission date 提交时间 |
| --- | --- | --- | --- |
| 1 | yitu_api_zh | 3.10 % | 2022.05 |
| 2 | bilibili_api_zh | 3.46 % | 2022.06 |
| 3 | microsoft_sdk_zh | 3.47% | 2022.05 |
| 4 | aispeech_api_zh | 3.63% | 2022.05 |
| 5 | aliyun_api | 3.81% | 2022.05 |
| 6 | iflytek_lfasr_api_zh | 4.05% | 2022.05 |
| 7 | tencent_api_zh | 4.06% | 2022.05 |
| 8 | baidu_pro_api_zh | 7.38% | 2022.05 |

---
## 6. Latest Leaderboard Report
![result](misc/SpeechIO_TIOBE_2022_05.png)

---

## Contacts
Email: leaderboard@speechio.ai
