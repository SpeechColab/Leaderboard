#!/usr/bin/env python3
import sys, os
import argparse
import yaml

if __name__ == '__main__':
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

  DATASETS = MountPoint(os.path.abspath('dataset'), '/app/speechio/leaderboard/dataset', 'ro')
  UTILS    = MountPoint(os.path.abspath('utils'),   '/app/speechio/leaderboard/utils')


  parser = argparse.ArgumentParser()
  parser.add_argument('--begin_stage', type=int, default=0, help='only run stages inside [begin, end)')
  parser.add_argument('--end_stage', type=int, default=100, help='only run stages inside [begin, end)')
  parser.add_argument('--repo', choices=['public', 'private'], default='public', type=str)
  parser.add_argument('submission_key', type=str)
  args = parser.parse_args()

  if args.begin_stage <= 1 and 1 < args.end_stage:
    # Download model from leaderboard model hub
    model_hub_url = F'oss://speechio-leaderboard/hub/{args.repo}/{args.submission_key}'
    work_dir = os.path.abspath(os.path.join('workspace', args.submission_key))
    cmd = F"./oss -c SAFEBOX/oss.cfg cp -ur {model_hub_url}/ {work_dir}"
    print(cmd, file=sys.stderr)
    os.system(cmd)

  if args.begin_stage <= 2 < args.end_stage:
    # build docker image
    docker_context = os.path.join(work_dir, 'docker')
    docker_file    = os.path.join(work_dir, 'docker', 'Dockerfile')
    docker_image = F'speechio/leaderboard:{args.repo}_{args.submission_key}'
    docker_build_cmd = F'docker build -f {docker_file} -t {docker_image} {docker_context}'
    print(docker_build_cmd, file=sys.stderr)
    os.system(docker_build_cmd)

  if args.begin_stage <= 3 < args.end_stage:
    # prepare working dir
    info_file_path = os.path.join(work_dir, 'info.yaml')
    with open(info_file_path, 'r') as info_file:
      info = yaml.safe_load(info_file)
      # prepare test sets
      with open(os.path.join(work_dir, 'test_sets'), 'w+') as f:
        for x in info['test_sets']:
          print(x, file=f)

  if args.begin_stage <= 4 < args.end_stage:
    # run docker benchmark
    docker_run_cmd = F'docker run {DATASETS.DockerMountOption()} {UTILS.DockerMountOption()} -v {work_dir}:/app/speechio/leaderboard/test_env {docker_image} /app/speechio/leaderboard/utils/benchmark.sh'
    print(docker_run_cmd, file=sys.stderr)
    os.system(docker_run_cmd)
