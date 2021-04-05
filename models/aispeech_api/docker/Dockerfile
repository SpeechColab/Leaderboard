FROM ubuntu:18.04
LABEL maintainer="jerry.jiayu.du@gmail.com"

RUN apt-get update && apt-get install -y --no-install-recommends \
        ca-certificates \
        python3.8 \
        curl && \
    rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/bin/python3.8 /usr/bin/python3

WORKDIR /app/speechio/leaderboard
