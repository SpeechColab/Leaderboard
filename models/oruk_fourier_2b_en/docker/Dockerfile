FROM continuumio/miniconda3:24.7.1-0
LABEL maintainer="nathan@oruk.ai"

RUN conda install -y -c conda-forge pynini=2.1.5 && \
    conda clean -afy && \
    pip install --no-cache-dir regex requests

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

WORKDIR /app/speechio/leaderboard
