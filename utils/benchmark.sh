#!/usr/bin/env bash
service_list="aispeech aliyun baidu_pro microsoft sogou tencent yitu"

testset_list=""
testset_list="$testset_list nba_cctv_commentator nba_lanqiurenwu"
testset_list="$testset_list children_cartoon"
testset_list="$testset_list pingshu_shantianfang xiangsheng_deyunshe talkshow_tucao"
testset_list="$testset_list short_video_movie short_video_food"
testset_list="$testset_list luoxiang_fakao zhangxuefeng_kaoyan"
testset_list="$testset_list story_fm startup_insider"
testset_list="$testset_list zhibo_wangzherongyao zhibo_daihuo laoluo_yulu"
testset_list="$testset_list luozhenyu liyongle"
testset_list="$testset_list luyu_yirixing tianxiazuqiu"
testset_list="$testset_list cctv_news"

max_num_utts=10
#----------------------------
export TEST_ENV=$(readlink -f .)

date=`date +%Y%m%d`
result=${TEST_ENV}/result
database=${TEST_ENV}/dataset

for testset in $testset_list; do
    for service in $service_list; do
        #cd service/$service
        echo "==>Testing Service:$service TEST_SET:$testset DATE:$date NUM_UTTS:$max_num_utts"
        # dir=$result/${date}__${service}__${testset}__${max_num_utts}
        # mkdir -p $dir
        # nohup ${TEST_ENV}/utils/test.sh $database/$testset $dir $max_num_utts >& $dir/log &
        sleep 0.1
        #cd -
    done
    wait
done
echo "Done"