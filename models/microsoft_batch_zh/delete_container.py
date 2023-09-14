#!/usr/bin/env python3
# doc: https://docs.azure.cn/zh-cn/storage/blobs/storage-quickstart-blobs-python?tabs=managed-identity%2Croles-azure-portal%2Csign-in-azure-cli

import sys
from azure.storage.blob import BlobServiceClient

with open('CONNECTION_STRING', 'r') as f:
    CONNECTION_STRING = f.readline().strip()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write("delete_container.py <container_name>\n")
        exit(-1)

    container_name = sys.argv[1]

    # Create the BlobServiceClient object
    blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)

    # Get the container
    container_client = blob_service_client.get_container_client(container=container_name)

    # Delete container
    container_client.delete_container()
    print("Delete container {container_name}".format(container_name=container_name))