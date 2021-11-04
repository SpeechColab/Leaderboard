FROM ubuntu:20.04
LABEL maintainer="aluminumbox@163.com"

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 \
        python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install grpcio==1.37.0 grpcio-tools==1.37.0 protobuf==3.15.8

# Use C.UTF-8 locale to avoid issues with ASCII encoding
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

WORKDIR /app/speechio/leaderboard