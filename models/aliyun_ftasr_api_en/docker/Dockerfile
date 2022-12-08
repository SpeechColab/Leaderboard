FROM ubuntu:20.04
LABEL maintainer="lzr265946@alibaba-inc.com"

RUN apt-get update && apt-get install -y --no-install-recommends \
        wget \
        python3 \
        python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install oss2 aliyun-python-sdk-core==2.13.3

# Use C.UTF-8 locale to avoid issues with ASCII encoding
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

WORKDIR /app/speechio/leaderboard
