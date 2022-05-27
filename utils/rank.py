#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Auther: Shaoji ZHANG 2022.05
#         Jiayu DU

import os
import glob
import json
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--begin', type = int, default = 1, help = 'testsets index begin [begin, end)')
    parser.add_argument('--end', type = int, default = 31, help = 'testsets index end [begin, end)')
    parser.add_argument('dir', type=str)
    args = parser.parse_args()

    test_sets = [ F'SPEECHIO_ASR_ZH{i:05d}' for i in range(args.begin, args.end) ]
    dir_pattern = os.path.join(args.dir, '*')

    service_ter_stats = {}
    testset_ter = {}

    for res_dir in glob.iglob(dir_pattern):
        date, service, test_set, max_utts = res_dir.split('__')
        with open(os.path.join(res_dir, 'RESULTS.txt'), encoding='utf-8') as f:
            for line in f:
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
                    if test_set in test_sets:
                        if testset_ter.get(test_set):
                            if testset_ter.get(test_set).get(service):
                                print(res_dir)
                            else:
                                testset_ter[test_set][service] = F'{100-TER:.2f},{TER:.2f},{n}:{H}:{R}:{max_utts},{date}'
                        else:
                            testset_ter[test_set] = {service : F'{100-TER:.2f},{TER:.2f},{n}:{H}:{R}:{max_utts},{date}'}

                        if service_ter_stats.get(service):
                            service_ter_stats[service]['ter_num'] += S + I + D
                            service_ter_stats[service]['ter_den'] += S + C + D
                        else:
                            service_ter_stats[service] = {'ter_num': S + I + D, 'ter_den': S + C + D}

    for test_set in sorted(testset_ter.keys()):
        print(F'--- {test_set} ---')
        for k, (service, result) in enumerate(sorted(testset_ter.get(test_set).items(), key=lambda x:float(x[1].split(',')[0]), reverse=True), 1):
            print(k, service, result)
        print()


    service_ter = {}
    for service in service_ter_stats:
        service_ter[service] = service_ter_stats.get(service).get('ter_num') / service_ter_stats.get(service).get('ter_den')

    print('*** OVERALL ***')
    for k, (service, ter) in enumerate(sorted(service_ter.items(), key=lambda x:x[1]), 1):
        print(k, service, f'{ter * 100:.2f}%')
    print()

