FROM python:3.7
LABEL maintainer="tonko22@gmail.com"

RUN apt-get update && apt-get install -y --no-install-recommends &&\
    rm -rf /var/lib/apt/lists/*

RUN pip3 install vosk

RUN ln -s /usr/bin/python3 /usr/bin/python

# Use C.UTF-8 locale to avoid issues with ASCII encoding
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8


WORKDIR /app/speechio/leaderboard
