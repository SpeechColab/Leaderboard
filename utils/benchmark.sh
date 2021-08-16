#!/usr/bin/env bash
# Copyright  2021  Jiayu DU

echo "---------- Benchmarking Started ----------"

if [ -z "LEADERBOARD" ]; then
    echo "$0: LEADERBOARD env variable is empty"
    exit 1
fi

stage=0
max_num_utts=2
. $LEADERBOARD/utils/parse_options.sh

if [ $# -ne 2 ]; then
    echo "Usage: $0 <model> <space_seperated_test_sets>"
    echo "options:"
    echo "  --stage <int>"
    echo "  --max-num-utts <int>"
    exit 1
fi

model=$1
test_sets="$2"

cd $LEADERBOARD/models/$model && echo $PWD

for x in $test_sets; do
    date=$(date +%Y%m%d)
    echo "<<<<< MODEL:$model  TEST_SET:$x  DATE:$date  NUM_UTTS:$max_num_utts >>>>>"

    dir=$LEADERBOARD/results/${date}__${model}__${x}__${max_num_utts}
    mkdir -p $dir

    if [ $stage -le 1 ]; then
        echo "$0 --> Generating test data in $dir"
        $LEADERBOARD/utils/generate_test_data.py \
            --max_num_utts $max_num_utts \
            $(readlink -f ${LEADERBOARD}/datasets/$x) \
            $dir
    fi

    if [ $stage -le 2 ]; then
        echo "$0 --> Recognizing in $dir"
        if [ -f 'SBI' ]; then
            chmod +x SBI
            chmod +x *
            ./SBI $dir/wav.scp $dir >& $dir/log.SBI
        else
            echo "$0: ERROR, cannot find SBI program"
        fi
    fi

    if [ $stage -le 3 ]; then
        language=$(grep language model.yaml | awk -F: '{print $NF}' | tr -d " ")
        echo "$0 --> Normalizing REF text ..."
        ${LEADERBOARD}/utils/tn_${language}.py \
            --has_key --to_upper \
            $dir/trans.txt \
            $dir/ref.txt

        echo "$0 --> Normalizing HYP text ..."
        ${LEADERBOARD}/utils/tn_${language}.py \
            --has_key --to_upper \
            $dir/raw_rec.txt \
            $dir/rec.txt
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

echo "---------- Benchmarking Done ----------"
