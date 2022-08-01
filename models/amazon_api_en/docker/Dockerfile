FROM ubuntu:20.04
LABEL maintainer="wang-rq19@mails.tsinghua.edu.cn"

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 \
        python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install boto3
RUN pip3 install amazon_transcribe
RUN pip3 install websocket_client
RUN pip3 install aiofile

# Use C.UTF-8 locale to avoid issues with ASCII encoding
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

WORKDIR /app/speechio/leaderboard
