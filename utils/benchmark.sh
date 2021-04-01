#!/usr/bin/env bash
max_num_utts=10
#----------------------------
#LEADERBOARD=/app/speechio/leaderboard
LEADERBOARD=/home/dophist/work/git/leaderboard/
TEST_SETS="MINI SPEECHIO_ASR_CN0001"
TEST_LANG="zh"

if [ -z $LEADERBOARD ] || [ -z $TEST_SETS ] || [ -z ! $TEST_LANG ]; then
    echo "ERROR, need LEADERBOARD & TEST_SETS & TEST_LANG env variables ."
    exit 1
fi

cd $LEADERBOARD/test_env && echo $PWD
stage=0

for testset in $TEST_SETS; do
    date=$(date +%Y%m%d)
    echo "========== Testing TEST_SET:$testset DATE:$date NUM_UTTS:$max_num_utts =========="

    dir=result/${date}__${testset}__${max_num_utts}
    mkdir -p $dir

    testset=$(readlink -f ${LEADERBOARD}/datasets/$testset)
    if [ $stage -le 1 ]; then
        echo "$0 --> Generating $testset data into $dir ..."
        $LEADERBOARD/utils/generate_test_data.py --max_num_utts $max_num_utts $testset $dir
    fi

    if [ $stage -le 2 ]; then
        echo "$0: --> Recognizing $test_set, LOG=$dir/log.MBI ..."
        if [ -f 'MBI' ]; then
            chmod +x MBI
            ./MBI $dir/wav.scp $dir >& $dir/log.MBI
        else
            echo "$0: ERROR, cannot find MBI program"
        fi
    fi

    if [ $stage -le 3 ]; then
        echo "$0 --> Normalizing REF text ..."
        ${LEADERBOARD}/utils/tn_${TEST_LANG}.py --has_key --to_upper $dir/trans.txt $dir/ref.txt

        echo "$0 --> Normalizing HYP text ..."
        ${LEADERBOARD}/utils/tn_${TEST_LANG}.py --has_key --to_upper $dir/raw_rec.txt $dir/rec.txt
        grep -v $'\t$' $dir/rec.txt > $dir/rec_non_empty.txt

        echo "$0 --> computing WER/CER and alignment ..."
        ${LEADERBOARD}/utils/asr-score \
            --tokenizer char \
            --ref $dir/ref.txt \
            --hyp $dir/rec_non_empty.txt \
            $dir/CHECK 1> $dir/CER
    fi

    sleep 1
done
echo "Done"
