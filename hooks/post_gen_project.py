import os
import shutil

print(os.getcwd())  # prints /absolute/path/to/{{cookiecutter.project_slug}}

def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)

use_gitlab = '{{cookiecutter.use_gitlab}}' == 'y'

if not use_gitlab:
    # remove top-level file inside the generated folder
    remove('.gitlab-ci.yml')