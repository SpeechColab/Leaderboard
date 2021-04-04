#!/usr/bin/env bash
# Copyright  2021  Jiayu DU

max_num_utts=2
#----------------------------
#LEADERBOARD=/app/speechio/leaderboard
#LEADERBOARD=/home/dophist/work/git/leaderboard/
#TEST_SETS="MINI SPEECHIO_ASR_ZH0001"
#TEST_LANG="zh"

if [ -z $LEADERBOARD ] || [ -z $TEST_SETS ] || [ -z $TEST_LANG ]; then
    echo "ERROR, need LEADERBOARD & TEST_SETS & TEST_LANG env variables."
    exit 1
fi

cd $LEADERBOARD/test_env && echo $PWD
stage=0

for testset in $TEST_SETS; do
    date=$(date +%Y%m%d)
    echo "========== Testing TEST_SET:$testset DATE:$date NUM_UTTS:$max_num_utts =========="

    dir=$LEADERBOARD/result/${date}__${testset}__${max_num_utts}
    mkdir -p $dir

    testset=$(readlink -f ${LEADERBOARD}/datasets/$testset)
    if [ $stage -le 1 ]; then
        echo "$0 --> Generating test data in $dir"
        $LEADERBOARD/utils/generate_test_data.py --max_num_utts $max_num_utts $testset $dir
    fi

    if [ $stage -le 2 ]; then
        echo "$0 --> Recognizing in $dir"
        if [ -f 'SBI' ]; then
            chmod +x SBI
            ./SBI $dir/wav.scp $dir >& $dir/log.SBI
        else
            echo "$0: ERROR, cannot find SBI program"
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
            $dir/CHECK | tee $dir/CER
    fi

    sleep 1
done
echo "Done"
