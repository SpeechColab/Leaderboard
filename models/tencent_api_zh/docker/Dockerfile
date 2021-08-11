FROM ubuntu:18.04
LABEL maintainer="jerry.jiayu.du@gmail.com"

RUN apt-get update && apt-get install -y --no-install-recommends \
        python \
        python3 \
        python-pip && \
    rm -rf /var/lib/apt/lists/*

RUN pip install tencentcloud-sdk-python

# Use C.UTF-8 locale to avoid issues with ASCII encoding
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

WORKDIR /app/speechio/leaderboard