#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Auther: Shaoji Zhang
#

import os
import glob
import json

WH_TEST_LIST = [ F'SPEECHIO_ASR_ZH{i:05d}' for i in range(1, 11) ]
BH_TEST_LIST = [ F'SPEECHIO_ASR_ZH{i:05d}' for i in range(1, 31) ]

dirpath = os.path.join('results', '2022_05', '*')
bh_all_dic = {}
wh_all_dic = {}
bh_dic = {}
wh_dic = {}
for dpath in glob.iglob(dirpath):
    date, service, test_set, max_utts = dpath.split('__')
    with open(os.path.join(dpath,'RESULTS.txt'),encoding='utf-8') as fp:
        for line in fp:
            if 'token_error_rate' in line:
                r = json.loads(line)
                TER = r['token_error_rate']
                R = r['num_ref_utts']
                H = r['num_hyp_utts']
                n = r['num_eval_utts']
                C = r['C']
                S = r['S']
                I = r['I']
                D = r['D']
                # buffer.append(F"{service},{test_set},{100-TER:.2f},{TER:.2f},{n}:{H}:{R}:{max_utts},{date}")
                if test_set in BH_TEST_LIST:
                    if bh_dic.get(test_set):
                        if bh_dic.get(test_set).get(service):
                            print(dpath)
                        else:
                            bh_dic[test_set][service] = F"{100-TER:.2f},{TER:.2f},{n}:{H}:{R}:{max_utts},{date}"
                    else:
                        bh_dic[test_set] = {service:F"{100-TER:.2f},{TER:.2f},{n}:{H}:{R}:{max_utts},{date}"}
                    if bh_all_dic.get(service):
                        bh_all_dic[service]['wrong'] += S + I + D
                        bh_all_dic[service]['corr'] += S + C + D
                    else:
                        bh_all_dic[service] = {'wrong': S + I + D,'corr': S + C + D}

                if test_set in WH_TEST_LIST:
                    if wh_dic.get(test_set):
                        if wh_dic.get(test_set).get(service):
                            print(dpath)
                        else:
                            wh_dic[test_set][service] = F"{100-TER:.2f},{TER:.2f},{n}:{H}:{R}:{max_utts},{date}"
                    else:
                        wh_dic[test_set] = {service:F"{100-TER:.2f},{TER:.2f},{n}:{H}:{R}:{max_utts},{date}"}

                    if wh_all_dic.get(service):
                        wh_all_dic[service]['wrong'] += S + I + D
                        wh_all_dic[service]['corr'] += S + C + D
                    else:
                        wh_all_dic[service] = {'wrong': S + I + D,'corr': S + C + D}



for test_set in wh_dic:
    service_result = sorted(wh_dic.get(test_set).items(),key=lambda x:float(x[1].split(',')[0]),reverse=True)
    # print(test_set)
    for result in service_result:
        print(result[0],result[1])


for test_set in bh_dic:
    service_result = sorted(bh_dic.get(test_set).items(),key=lambda x:float(x[1].split(',')[0]),reverse=True)
    # print(F"{test_set},{service_result[0][0]},{service_result[0][1]}")
    # print(test_set)
    for result in service_result:
        print(result[0], result[1])


####所有识别结果一起排名#####
wh_ter_dic = {}
bh_ter_dic = {}
# print(wh_all_dic)
for service in wh_all_dic:
    wrong = wh_all_dic.get(service).get('wrong')
    corr = wh_all_dic.get(service).get('corr')
    wh_ter_dic[service] = wrong/corr

print('----- released test sets -----')
for k, (service, ter) in enumerate(sorted(wh_ter_dic.items(),key=lambda x:x[1]), 1):
    print(k, service, f'{ter * 100:.2f}%')

for service in bh_all_dic:
    wrong = bh_all_dic.get(service).get('wrong')
    corr = bh_all_dic.get(service).get('corr')
    bh_ter_dic[service] = wrong / corr

print('----- not released test sets -----')
for k, (service, ter) in enumerate(sorted(bh_ter_dic.items(), key=lambda x: x[1]), 1):
    print(k, service, f'{ter * 100:.2f}%')
