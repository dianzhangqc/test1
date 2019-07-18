import os
import subprocess

repo_path = subprocess.Popen(['git', 'rev-parse', '--show-toplevel'], stdout=subprocess.PIPE).communicate()[0].rstrip()
print (repo_path)

cmd = ['git', 'clone', 'repo_path', 'tempo_repo']
subprocess.call(cmd)
