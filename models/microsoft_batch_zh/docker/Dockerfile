FROM ubuntu:20.04
LABEL maintainer="v-huilia@microsoft.com"

COPY python-client /app/speechio/leaderboard/python-client

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 \
        python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install requests

RUN pip3 install azure-storage-blob azure-identity

RUN pip3 install /app/speechio/leaderboard/python-client

# Use C.UTF-8 locale to avoid issues with ASCII encoding
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

WORKDIR /app/speechio/leaderboard
