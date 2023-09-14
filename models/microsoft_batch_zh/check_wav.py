#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import codecs
import datetime
import os
import sys
import time
from azure.storage.blob import (
    BlobServiceClient,
    BlobClient,
    ResourceTypes,
    AccountSasPermissions,
    generate_account_sas
)

MAX_RETRY = 10
RETRY_INTERVAL = 5.0

with open('CONNECTION_STRING', 'r') as f:
    CONNECTION_STRING = f.readline().strip()

with open('STORAGE_ACCOUNT', 'r') as f:
    STORAGE_ACCOUNT = f.readline().strip()

with open('STORAGE_KEY', 'r') as f:
    STORAGE_KEY = f.readline().strip()


def create_account_sas():

    # Create an account SAS that's valid for one day
    start_time = datetime.datetime.now(datetime.timezone.utc)
    expiry_time = start_time + datetime.timedelta(days=1)

    # Define the SAS token permissions
    sas_permissions = AccountSasPermissions(read=True)

    # Define the SAS token resource types
    # For this example, we grant access to service-level APIs
    sas_resource_types = ResourceTypes(service=True, container=True, object=True)

    sas_token = generate_account_sas(
        account_name=STORAGE_ACCOUNT,
        account_key=STORAGE_KEY,
        resource_types=sas_resource_types,
        permission=sas_permissions,
        expiry=expiry_time,
        start=start_time
    )

    return sas_token


def get_share_url():

    # Create SAS
    sas_token = create_account_sas()
    sas_url = '{blob_client_url}?{sas_token}'.format(blob_client_url=blob_client.url, sas_token=sas_token)
    # Share
    BlobClient.from_blob_url(blob_url=sas_url)

    return sas_url


def retry_upload(wav_id, wav_path, container_name, times):

    # Retry upload wav
    blob_client = blob_service_client.get_blob_client(container=container_name+"/wav", blob=os.path.basename(wav_path))
    with open(file=wav_path, mode="rb") as data:
        blob_client.upload_blob(data)

    retry_flag = False
    exist = blob_client.exists()
    if exist:
        print('Checked： {wav_id} {wav_path} retried successfully'.format(wav_id=wav_id, wav_path=wav_path))
        sas_url = get_share_url()
        wav_blob_scp.write(wav_id + "\t" + sas_url)
        retry_flag = True
        return retry_flag
    elif times > 0:
        time.sleep(RETRY_INTERVAL)
        print("Checked: {wav_id} {wav_path} object not exist, will retry upload {times} times.".format(wav_id=wav_id, wav_path=wav_path))
        retry_flag = retry_upload(wav_id, wav_path, container_name, times=times-1)

    return retry_flag


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.stderr.write("check_wav.py <container_name> <wav_in_scp> <wav_loss_scp> <wav_blob_scp>\n")
        exit(-1)

    container_name = sys.argv[1]
    wav_in_scp = codecs.open(sys.argv[2], 'r',  'utf8')
    wav_loss_scp = codecs.open(sys.argv[3], 'w+', 'utf8')
    wav_blob_scp = codecs.open(sys.argv[4], 'w+', 'utf8')

    # Create the BlobServiceClient object
    blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)

    # Get container
    container_client = blob_service_client.get_container_client(container=container_name)

    # Check wav
    for meta in wav_in_scp:
        wav_meta = meta.split()
        wav_id = wav_meta[0]
        wav_path = wav_meta[1]
        blob_client = container_client.get_blob_client("wav/"+os.path.basename(wav_path))
        exist = blob_client.exists()
        if exist:
            print('Checked: {wav_id} {wav_path}.'.format(wav_id=wav_id, wav_path=wav_path))
            sas_url = get_share_url()
            wav_blob_scp.write(wav_id + "\t" + sas_url+"\n")
        else:
            print('Checked: {wav_id} {wav_path} object not exist.'.format(wav_id=wav_id, wav_path=wav_path))
            retry_flag = retry_upload(wav_id, wav_path, container_name, MAX_RETRY)
            if not retry_flag:
                wav_loss_scp.write(meta)
                wav_loss_scp.flush()

    wav_in_scp.close()
    wav_loss_scp.close()
    wav_blob_scp.close()