import os
import subprocess

def main(cmd: str, base_dir: str):
  for root, dirs, files in os.walk(base_dir):
    for f in files:
      full_cmd = cmd.replace('<FILE>', os.path.realpath(os.path.join(root, f)))
      res = subprocess.run(full_cmd, shell=True, capture_output=True)
      if res.returncode:
        print(res.stderr.decode())
      else:
        print(res.stdout.decode())


if __name__ == "__main__":
  import argparse
  p = argparse.ArgumentParser()
  p.add_argument('cmd', help='Shell one-liner to run on every file')
  p.add_argument(
    'base_dir',
    default='/',
    help='Shady will run the command on every file in this directory and all subdirectories. (default: /)'
  )

  args = p.parse_args()
  main(**vars(args))
