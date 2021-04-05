
FROM ubuntu:18.04
LABEL maintainer="jerry.jiayu.du@gmail.com"

RUN apt-get update && apt-get install -y --no-install-recommends \
        python \
        python3 \
        python-pip && \
    rm -rf /var/lib/apt/lists/*

RUN pip install requests==2.21.0

WORKDIR /app/speechio/leaderboard