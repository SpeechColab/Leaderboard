FROM ubuntu:20.04
LABEL maintainer="jerry.jiayu.du@gmail.com"

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3 \
        python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install boto3
RUN pip3 install amazon_transcribe
RUN pip3 install websocket_client
RUN pip3 install aiofile
RUN pip3 install azure-cognitiveservices-speech
RUN pip3 install requests
RUN pip3 install nemo_toolkit
RUN pip3 install pynini 
RUN pip3 install pytorch_lightning
RUN pip3 install hydra-core
RUN pip3 install transformers
RUN pip3 install pandas
RUN pip3 install sentencepiece
RUN pip3 install youtokentome
RUN pip3 install sacremoses
# Use C.UTF-8 locale to avoid issues with ASCII encoding
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV AWS_ACCESS_KEY_ID=test
ENV AWS_SECRET_ACCESS_KEY=test
ENV AWS_DEFAULT_REGION=test
WORKDIR /app/speechio/leaderboard
