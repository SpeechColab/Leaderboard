model=speechio_kaldi
leaderboard=$(readlink -f .)
test_sets="MINI SPEECHIO_ASR_ZH00000"
test_lang=zh
rm test_env
ln -s models/$model test_env
LEADERBOARD=$leaderboard TEST_SETS="$test_sets" TEST_LANG=$test_lang  utils/benchmark.sh
