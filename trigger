#!/usr/bin/env python3
import sys, os
import argparse
import yaml

class MountPoint:
  def __init__(self, src, dst, mode = ''):
    self.src = src
    self.dst = dst
    self.mode = mode

  def DockerMountOption(self):
    if self.mode:
      return F'-v {self.src}:{self.dst}:{self.mode}'
    else:
      return F'-v {self.src}:{self.dst}'

def fix_oss_url(oss_url):
  if oss_url.endswith('/'):
    return oss_url
  else:
    return oss_url + '/'

DATASETS = MountPoint('/Users/jerry/work/tiobe/test_env/dataset', '/app/speechio/leaderboard/dataset', 'ro')
UTILS = MountPoint(os.path.abspath('utils'), '/app/speechio/leaderboard/utils')

parser = argparse.ArgumentParser()
parser.add_argument('submission_key', type=str)
args = parser.parse_args()

# STEP: submission check 
info_file_path = os.path.join('submissions', args.submission_key, 'info.yaml')
assert(os.path.isfile(info_file_path))
info = yaml.safe_load(open(info_file_path, 'r'))
assert(info['key'] == args.submission_key)
print(F'submission info: {info}', file=sys.stderr)

# STEP: download model from leaderboard hub
work_dir = os.path.abspath(os.path.join('workspace', args.submission_key))
cmd = F"./oss cp -ur {fix_oss_url(info['url'])} {work_dir}"
print(cmd, file=sys.stderr)
#os.system(cmd)

# STEP: build docker image
docker_context = os.path.join(work_dir, 'docker')
docker_file    = os.path.join(work_dir, 'docker', 'Dockerfile')
docker_image = F'speechio/leaderboard:{args.submission_key}'
docker_build_cmd = F'docker build -f {docker_file} -t {docker_image} {docker_context}'
print(docker_build_cmd, file=sys.stderr)
os.system(docker_build_cmd)

with open(os.path.join(work_dir, 'test_sets'), 'w+') as f:
  for x in info['test_sets']:
    print(x, file=f)

# instantiate a benchmark container
docker_run_cmd = F'docker run {DATASETS.DockerMountOption} {UTILS.DockerMountOption} -v {work_dir}:/app/speechio/leaderboard/test_env {docker_image} /app/speechio/leaderboard/utils/benchmark.sh'
print(docker_run_cmd, file=sys.stderr)
os.system(docker_run_cmd)
