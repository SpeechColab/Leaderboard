FROM ubuntu:18.04
LABEL maintainer="jerry.jiayu.du@gmail.com"

RUN apt-get update && apt-get install -y --no-install-recommends \
        g++ \
        make \
        automake \
        autoconf \
        cmake \
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
RUN git clone --depth 1 https://github.com/kaldi-asr/kaldi.git ${KALDI_ROOT} && \
    cd ${KALDI_ROOT}/tools && \
    ./extras/install_mkl.sh && \
    make -j $(nproc) && \
    cd ${KALDI_ROOT} && \
    mkdir -p build && cd build && \
    cmake -DMATHLIB=MKL -DBUILD_SHARED_LIBS=ON -DCMAKE_INSTALL_PREFIX=${KALDI_ROOT}/dist .. && \
    cmake --build . --target install -- -j $(nproc) && \
    find /opt/kaldi -type f \( -name "*.o" -o -name "*.la" -o -name "*.a" \) -exec rm {} \; && \
    find /opt/intel -type f -name "*.a" -exec rm {} \; && \
    find /opt/intel -type f -regex '.*\(_mc.?\|_mic\|_thread\|_ilp64\)\.so' -exec rm {} \; && \
    rm -rf ${KALDI_ROOT}/.git && \
    rm -rf ${KALDI_ROOT}/build
ENV PATH=$PATH:$KALDI_ROOT/dist/bin

WORKDIR /app/speechio/leaderboard
