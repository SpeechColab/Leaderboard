#!/usr/bin/env python3
# coding=utf-8
"""
this test script is based on the official demo release:
https://xfyun-doc.cn-bj.ufileos.com/1564736425808301/weblfasr_python3_demo.zip
"""
import base64
import codecs
import hashlib
import hmac
import json
import os
import sys
import time

import requests

# interface name
API_HOST = 'https://raasr.xfyun.cn/api'

# get message by this address—> https://console.xfyun.cn/services/lfasr
APP_ID = ''
with open('APP_ID', 'r') as f:
    APP_ID = f.readline().strip()

SECRET_KEY = ''
with open('SECRET_KEY', 'r') as f:
    SECRET_KEY = f.readline().strip()

MAX_WORKER = 10

api_prepare = '/prepare'
api_upload = '/upload'
api_merge = '/merge'
api_get_progress = '/getProgress'
api_get_result = '/getResult'
# slice_size
slice_size = 10485760

# more parameter can be found in address—> https://doc.xfyun.cn/rest_api/%E8%AF%AD%E9%9F%B3%E8%BD%AC%E5%86%99.html
max_alternatives = 0


class SliceIdGenerator:
    def __init__(self):
        self.__ch = 'aaaaaaaaa`'

    def get_next_slice_id(self):
        ch = self.__ch
        j = len(ch) - 1
        while j >= 0:
            cj = ch[j]
            if cj != 'z':
                ch = ch[:j] + chr(ord(cj) + 1) + ch[j + 1:]
                break
            else:
                ch = ch[:j] + 'a' + ch[j + 1:]
                j = j - 1
        self.__ch = ch
        return self.__ch


def gene_request(api_name, data, files=None, headers=None):
    response = requests.post(API_HOST + api_name, data=data, files=files, headers=headers)
    result = json.loads(response.text)
    if result["ok"] == 0:
        print("{} success:".format(api_name) + str(result))
        if api_name == '/getResult':
            # print(result)
            data_list = json.loads(result.get('data'))
            temp_result = ''
            for tmp in data_list:
                temp_result += tmp.get('onebest')
            # print(temp_result)
            return temp_result
        return result
    else:
        print("{} error:".format(api_name) + str(result))
        return ''


class RequestApi(object):
    def __init__(self, appid, secret_key, upload_file_path):
        self.appid = appid
        self.secret_key = secret_key
        self.upload_file_path = upload_file_path

    # more parameter can be found in address—> https://doc.xfyun.cn/rest_api/%E8%AF%AD%E9%9F%B3%E8%BD%AC%E5%86%99.html
    def gene_params(self, apiname, taskid=None, slice_id=None):
        appid = self.appid
        secret_key = self.secret_key
        upload_file_path = self.upload_file_path
        ts = str(int(time.time()))
        m2 = hashlib.md5()
        m2.update((appid + ts).encode('utf-8'))
        md5 = m2.hexdigest()
        md5 = bytes(md5, encoding='utf-8')
        signa = hmac.new(secret_key.encode('utf-8'), md5, hashlib.sha1).digest()
        signa = base64.b64encode(signa)
        signa = str(signa, 'utf-8')
        file_len = os.path.getsize(upload_file_path)
        file_name = os.path.basename(upload_file_path)
        param_dict = {}

        if apiname == api_prepare:
            # slice_num indicates the number of fragments
            slice_num = int(file_len / slice_size) + (0 if (file_len % slice_size == 0) else 1)
            param_dict['app_id'] = appid
            param_dict['signa'] = signa
            param_dict['ts'] = ts
            param_dict['file_len'] = str(file_len)
            param_dict['file_name'] = file_name
            param_dict['slice_num'] = str(slice_num)
        elif apiname == api_upload:
            param_dict['app_id'] = appid
            param_dict['signa'] = signa
            param_dict['ts'] = ts
            param_dict['task_id'] = taskid
            param_dict['slice_id'] = slice_id
        elif apiname == api_merge:
            param_dict['app_id'] = appid
            param_dict['signa'] = signa
            param_dict['ts'] = ts
            param_dict['task_id'] = taskid
            param_dict['file_name'] = file_name
        elif apiname == api_get_progress or apiname == api_get_result:
            param_dict['app_id'] = appid
            param_dict['signa'] = signa
            param_dict['ts'] = ts
            param_dict['task_id'] = taskid
        return param_dict

    # return parameter Meaning—> https://doc.xfyun.cn/rest_api/%E8%AF%AD%E9%9F%B3%E8%BD%AC%E5%86%99.html

    # prepare
    def prepare_request(self):
        return gene_request(api_name=api_prepare,
                            data=self.gene_params(api_prepare))

    # upload
    def upload_request(self, taskid, upload_file_path):
        file_object = open(upload_file_path, 'rb')
        try:
            index = 1
            sig = SliceIdGenerator()
            while True:
                content = file_object.read(slice_size)
                if not content or len(content) == 0:
                    break
                files = {
                    "filename": self.gene_params(api_upload).get("slice_id"),
                    "content": content
                }
                response = gene_request(api_upload,
                                        data=self.gene_params(api_upload, taskid=taskid,
                                                              slice_id=sig.get_next_slice_id()),
                                        files=files)
                if response.get('ok') != 0:
                    # upload slice fail
                    print('upload slice fail, response: ' + str(response))
                    return False
                print('upload slice ' + str(index) + ' success')
                index += 1
        finally:
            'file index:' + str(file_object.tell())
            file_object.close()
        return True

    # merge
    def merge_request(self, taskid):
        return gene_request(api_merge, data=self.gene_params(api_merge, taskid=taskid))

    # get progress
    def get_progress_request(self, taskid):
        return gene_request(api_get_progress, data=self.gene_params(api_get_progress, taskid=taskid))

    # get result
    def get_result_request(self, taskid):
        return gene_request(api_get_result, data=self.gene_params(api_get_result, taskid=taskid))

    def all_api_request(self):
        # prepare
        pre_result = self.prepare_request()
        # print(type(pre_result))
        try:
            taskid = pre_result.get('data')

            # Shard to upload
            self.upload_request(taskid=taskid, upload_file_path=self.upload_file_path)
            # merge
            self.merge_request(taskid=taskid)
            # get progress
            while True:
                # the task progress is obtained every 2 seconds
                progress = self.get_progress_request(taskid)
                progress_dic = progress
                if progress_dic.get('err_no') != 0 and progress_dic.get('err_no') != 26605:
                    print('task error: ' + progress_dic.get('failed'))
                    return
                else:
                    data = progress_dic.get('data')
                    task_status = json.loads(data)
                    if task_status['status'] == 9:
                        print('task ' + taskid + ' finished')
                        break
                    print('The task ' + taskid + ' is in processing, task status: ' + str(data))

                # the task progress is obtained every 2 seconds
                time.sleep(2)
        except Exception:
            return ''
        # get result
        return self.get_result_request(taskid=taskid)


def tt(temp):
    temp = temp.strip()
    # print(temp)
    if len(temp.split()) == 2:  # source_info_list format: "key\taudio"
        key, audio = temp.split(maxsplit=1)
        sys.stderr.write('\tkey:' + key + '\taudio:' + audio + '\n')
        sys.stderr.flush()

        api = RequestApi(appid=APP_ID, secret_key=SECRET_KEY, upload_file_path=audio)
        text = api.all_api_request()

        # print('text--------->', text)
        print(f'{key} is success')
        return '{0}'.format(key + '\t' + text + '\n')

    else:
        return '{0}'.format("Invalid line: " + temp + "\n")


from concurrent.futures import ThreadPoolExecutor, as_completed


def main():
    source_info_list = codecs.open(sys.argv[1], 'r', 'utf8')
    result_file_path = codecs.open(sys.argv[2], 'w+', 'utf8')
    # audio_num = len(source_info_list.readlines())
    # Enable a thread pool of up to 10 threads
    executor = ThreadPoolExecutor(max_workers=MAX_WORKER)
    # Create a task and add it to the list
    all_task = [executor.submit(tt, (temp)) for temp in source_info_list]
    for future in as_completed(all_task):
        data = future.result()
        result_file_path.write(data)
        result_file_path.flush()
    source_info_list.close()
    result_file_path.close()


'''
If the requests module reports an error: "NoneType" object has no attribute 'read', try updating the requests
module to 2.20.0 or later
'''
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("asr_api.py <in_scp> <out_trans>")
        exit(-1)
    main()
