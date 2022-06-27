FROM ubuntu:20.04
LABEL maintainer="xuanwu@bilibili.com"

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 \
        python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Use C.UTF-8 locale to avoid issues with ASCII encoding
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
RUN pip3 install requests==2.21.0

WORKDIR /app/speechio/leaderboard
