FROM ubuntu:18.04
LABEL maintainer="jerry.ejwt@gmail.com"

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        g++ \
        make \
        automake \
        autoconf \
        bzip2 \
        unzip \
        wget \
        sox \
        libtool \
        git \
        subversion \
        python2.7 \
        python3 \
        zlib1g-dev \
        ca-certificates \
        gfortran \
        patch \
        ffmpeg \
	    vim && \
    rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/bin/python3 /usr/bin/python

ENV MKLROOT=/opt/intel/mkl KALDI_ROOT=/opt/kaldi
RUN git clone --depth 1 https://github.com/kaldi-asr/kaldi.git ${KALDI_ROOT} #EOL
RUN cd ${KALDI_ROOT}/tools && ./extras/install_mkl.sh
RUN cd ${KALDI_ROOT}/tools && make -j $(nproc)
RUN cd ${KALDI_ROOT}/src && \
    ./configure --shared && \
    make depend -j $(nproc) && \
    make -j $(nproc) && \
    find ${KALDI_ROOT} -type f \( -name "*.o" -o -name "*.la" -o -name "*.a" \) -exec rm {} \; && \
    find /opt/intel -type f -name "*.a" -exec rm {} \; && \
    find /opt/intel -type f -regex '.*\(_mc.?\|_mic\|_thread\|_ilp64\)\.so' -exec rm {} \; && \
    rm -rf ${KALDI_ROOT}/.git

ENV PATH=\
$KALDI_ROOT/tools/openfst/bin:$PATH:\
${KALDI_ROOT}/src/bin:\
${KALDI_ROOT}/src/chainbin:\
${KALDI_ROOT}/src/featbin:\
${KALDI_ROOT}/src/fgmmbin:\
${KALDI_ROOT}/src/fstbin:\
${KALDI_ROOT}/src/gmmbin:\
${KALDI_ROOT}/src/ivectorbin:\
${KALDI_ROOT}/src/kwsbin:\
${KALDI_ROOT}/src/latbin:\
${KALDI_ROOT}/src/lmbin:\
${KALDI_ROOT}/src/nnet2bin:\
${KALDI_ROOT}/src/nnet3bin:\
${KALDI_ROOT}/src/nnetbin:\
${KALDI_ROOT}/src/online2bin:\
${KALDI_ROOT}/src/onlinebin:\
${KALDI_ROOT}/src/rnnlmbin:\
${KALDI_ROOT}/src/sgmm2bin:\
${KALDI_ROOT}/src/sgmmbin:\
${KALDI_ROOT}/src/tfrnnlmbin:\
${KALDI_ROOT}/src/cudadecoderbin:\
$PATH

SHELL ["/bin/bash", "-c"] 
ENV LC_ALL=C

WORKDIR /app/speechio/leaderboard

