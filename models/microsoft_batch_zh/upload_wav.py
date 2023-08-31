#!/usr/bin/env python3
# doc: https://docs.azure.cn/zh-cn/storage/blobs/storage-quickstart-blobs-python?tabs=managed-identity%2Croles-azure-portal%2Csign-in-azure-cli

import codecs
import os
import sys
import time
from azure.storage.blob import BlobServiceClient

MAX_RETRY = 10

with open('CONNECTION_STRING', 'r') as f:
    CONNECTION_STRING = f.readline().strip()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.stderr.write("upload_wav.py <wav_in_scp> <container_name>\n")
        exit(-1)

    wav_dict = {}
    wav_in_scp = codecs.open(sys.argv[1], 'r',  'utf8')
    container_name = sys.argv[2]

    # Get meta
    for meta in wav_in_scp:
        wav_meta = meta.split()
        wav_id = wav_meta[0]
        wav_path = wav_meta[1]
        wav_dict[wav_id] = wav_path

    # Create the BlobServiceClient object
    print("Create container {container_name}".format(container_name=container_name))
    blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)

    # Create the container
    container_client = blob_service_client.create_container(container_name)

    time.sleep(5)

    # Upload wav
    for wav_id, wav_path in wav_dict.items():

        blob_client = blob_service_client.get_blob_client(container=container_name+"/wav", blob=os.path.basename(wav_path))
        with open(file=wav_path, mode="rb") as data:
            blob_client.upload_blob(data)
        print("Uploaded: {wav_id}\t{wav_path}".format(wav_id=wav_id, wav_path=wav_path) )
