#!/usr/bin/env bash
max_num_utts=10
#----------------------------
#LEADERBOARD=/app/speechio/leaderboard
LEADERBOARD=/home/dophist/work/git/leaderboard/
TEST_SETS="MINI SPEECHIO_ASR_CN0001"

if [ -z $LEADERBOARD ] || [ -z $TEST_SETS ]; then
    echo "ERROR, variable LEADERBOARD or TEST_SETS empty."
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
        echo "$0: Generating test data from $testset to $dir"
        $LEADERBOARD/utils/generate_test_data.py --max_num_utts $max_num_utts $testset $dir
    fi

    if [ $stage -le 2 ]; then
        echo "$0: --> recognizing ... log in $dir/log.MBI"
        if [ -f 'MBI' ]; then
            chmod +x MBI
            ./MBI $dir/wav.scp $dir >& $dir/log.MBI
        else
            echo "$0: ERROR, cannot find MBI program id $dir"
        fi
    fi

    if [ $stage -le 3 ]; then
        echo "$0: --> preparing reference text for WER calculation..."
        ${LEADERBOARD}/utils/cn_tn.py --has_key --to_upper $dir/trans.txt $dir/ref.txt

        echo "$0: --> preparing hypothesis text for WER calculation ..."
        ${LEADERBOARD}/utils/cn_tn.py --has_key --to_upper $dir/raw_rec.txt $dir/rec.txt
        grep -v $'\t$' $dir/rec.txt > $dir/rec_present.txt # remove empty utts from hypothesis

        echo "$0: --> computing WER/CER and alignment ..."
        ${LEADERBOARD}/utils/asr-score \
            --tokenizer char \
            --ref $dir/ref.txt \
            --hyp $dir/rec_present.txt \
            $dir/CHECK 1> $dir/CER
    fi

    sleep 1
done
echo "Done"
