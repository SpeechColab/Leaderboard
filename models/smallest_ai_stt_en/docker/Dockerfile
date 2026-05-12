FROM --platform=linux/amd64 continuumio/miniconda3:23.10.0-1
LABEL maintainer="harshitajain@smallest.ai"

RUN conda install -y -c conda-forge python=3.8 pynini regex && \
    pip install --no-cache-dir requests websockets && \
    conda clean -afy

RUN ln -sf /opt/conda/bin/python3 /usr/bin/python3

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

WORKDIR /app/speechio/leaderboard
