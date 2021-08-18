FROM ubuntu:latest
LABEL maintainer="binbzha@qq.com"
ENV DEBIAN_FRONTEND=noninteractive

RUN sed -i s@/archive.ubuntu.com/@/mirrors.tuna.tsinghua.edu.cn/@g /etc/apt/sources.list
RUN apt-get update && apt-get install -y --no-install-recommends \
        ca-certificates \
        curl \
        python3 \
        git \
        cmake \
        build-essential && \
    rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/bin/python3 /usr/bin/python

ENV WENET_ROOT=/home/wenet
RUN git clone https://github.com/mobvoi/wenet.git ${WENET_ROOT}

RUN sed -i 's#https://download.pytorch.org/libtorch/cpu/#http://mobvoi-speech-public.ufile.ucloud.cn/public/wenet/mirros/libtorch/#g' ${WENET_ROOT}/runtime/server/x86/CMakeLists.txt

ENV WENET_BUILD=$WENET_ROOT/runtime/server/x86/build

RUN mkdir ${WENET_BUILD} && cd ${WENET_BUILD} && cmake .. && cmake --build .

ENV PATH=$WENET_BUILD:$PATH

SHELL ["/bin/bash", "-c"]

WORKDIR /app/speechio/leaderboard
