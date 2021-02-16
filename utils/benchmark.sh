#!/usr/bin/env bash
cd /app/speechio/leaderboard/test_env
echo $PWD

service_list=$(cat submission_key)
testset_list=$(cat test_sets)
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
        dir=${date}__${service}__${testset}__${max_num_utts}
        mkdir -p $dir
        echo "MBI" > $dir/log
        # nohup ${TEST_ENV}/utils/test.sh $database/$testset $dir $max_num_utts >& $dir/log &
        sleep 0.5
        #cd -
    done
    wait
done
echo "Done"