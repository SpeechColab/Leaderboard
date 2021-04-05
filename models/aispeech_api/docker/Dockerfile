FROM ubuntu:18.04
LABEL maintainer="jerry.jiayu.du@gmail.com"

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 \
        curl && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app/speechio/leaderboard