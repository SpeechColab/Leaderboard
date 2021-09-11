FROM python:3.7
LABEL maintainer="tonko22@gmail.com"

RUN apt-get update && apt-get install -y --no-install-recommends &&\
    rm -rf /var/lib/apt/lists/*
# RUN apt-get install -y tree

RUN ln -s /usr/bin/python3 /usr/bin/python

RUN pip3 install vosk
RUN git clone https://github.com/alphacep/vosk-api
RUN ls -la
RUN wget https://alphacephei.com/vosk/models/vosk-model-cn-0.1.zip -P vosk-api/python/example/
RUN unzip vosk-api/python/example/vosk-model-cn-0.1.zip -d vosk-api/python/example/
RUN ls -la vosk-api/python/example/

RUN ls -la
# mv vosk-model-cn-0.1 model \
# ls -la model/ \
# cd ../../../ \

# Use C.UTF-8 locale to avoid issues with ASCII encoding
# ENV LC_ALL=C
# ENV LANG=C.UTF-8


WORKDIR /app/speechio/leaderboard
RUN ls -la
RUN ls -la /vosk-api/
