#!/usr/bin/env bash
max_num_utts=10
#----------------------------
LEADERBOARD=/app/speechio/leaderboard
cd $LEADERBOARD/test_env && echo $PWD

for testset in $(cat test_sets); do
    date=$(date +%Y%m%d)
    echo "$0 --> Testing TEST_SET:$testset DATE:$date NUM_UTTS:$max_num_utts"
    dir=result/${date}__${testset}__${max_num_utts}
    mkdir -p $dir

    #nohup ${LEADERBOARD}/utils/test.sh $database/$testset $dir $max_num_utts >& $dir/log &

    testset=$(readlink -f ${LEADERBOARD}/dataset/$testset)
    n=$(wc -l ${testset}/wav.scp | awk '{print $1}')
    if [ $n -gt $max_num_utts ]; then
        n=$max_num_utts
    fi

    stage=0
    if [ ! -f ${testset}/wav.scp ] || [ ! -f ${testset}/trans.txt ]; then
        echo "$0: ERROR, missing wav.scp or trans.txt in test set"
        exit 1;
    fi

    if [ $stage -le 1 ]; then
        echo "$0: --> preparing test set from $testset to $dir"
        awk -v d=$testset '{print $1"\t"d"/"$2}' ${testset}/wav.scp | head -n $n > $dir/wav.scp
        awk '{print $1}' $dir/wav.scp > $dir/keys

        cat /dev/null > $dir/trans.txt
        for key in `cat $dir/keys`; do
            grep -- "$key[[:space:]]" ${testset}/trans.txt >> $dir/trans.txt
        done

        num_wavs=`cat $dir/wav.scp | wc -l`
        num_trans=`cat $dir/trans.txt | wc -l`
        if [ $num_wavs != $num_trans ]; then
            echo "$0: ERROR, found wavs without trans, wavs:$num_wavs, trans:$num_trans"
            exit -1
        else
            echo "  num_wavs:$num_wavs, num_trans:$num_trans"
        fi
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
        COMPUTE_WER=compute-wer
        ALIGN_TEXT=align-text
        echo "$0: --> preparing reference for WER computation..."
        python3 ${LEADERBOARD}/utils/cn_tn.py --has_key --to_upper $dir/trans.txt $dir/tmp.ref_tn.txt  # TN
        python3 ${LEADERBOARD}/utils/split_to_char.py $dir/tmp.ref_tn.txt $dir/ref.txt

        echo "$0: --> preparing recognition text for WER computation ..."
        python3 ${LEADERBOARD}/utils/cn_tn.py --has_key --to_upper $dir/raw_rec.txt $dir/raw_rec_tn.txt
        python3 ${LEADERBOARD}/utils/split_to_char.py $dir/raw_rec_tn.txt $dir/rec.txt
        grep -v $'\t$' $dir/rec.txt > $dir/rec_present.txt # filter away empty recognition result
        rm $dir/tmp.*

        echo "$0: --> computing CER and alignment ..."
        $COMPUTE_WER --mode=present --text=true ark,t:$dir/ref.txt ark,t:$dir/rec.txt > $dir/CER
        $ALIGN_TEXT ark,t:$dir/ref.txt ark,t:$dir/rec.txt ark,t:$dir/align.txt
        echo ""
        $COMPUTE_WER --mode=present --text=true ark,t:$dir/ref.txt ark,t:$dir/rec_present.txt > $dir/CER_present
        $ALIGN_TEXT ark,t:$dir/ref.txt ark,t:$dir/rec_present.txt ark,t:$dir/align_present.txt

        echo "$0: --> Getting pretty alignment ..."
        ${LEADERBOARD}/utils/prettify_align.py $dir/align_present.txt $dir/CHECK.txt
    fi

    sleep 1
done
echo "Done"