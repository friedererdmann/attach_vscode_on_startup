import sys
import os
import inspect
import importlib


def get_current_path():
    current_file = os.path.abspath(inspect.getsourcefile(get_current_path))
    path, _ = os.path.split(current_file)
    return path


def get_venv_site_packages():
    return os.path.join(get_current_path(), 'env', 'Lib', 'site-packages')


sys.path.append(get_venv_site_packages())

import ptvsd
ptvsd.enable_attach(address=("localhost", 7740), redirect_output=True)
ptvsd.wait_for_attach()
print("Listening on port 7740")


### ONLY NECESSARY IF YOU EXPECT YOUR CODE TO RUN AT STARTUP
path, script_ext = os.path.split(os.environ.get("SCRIPT_FILE"))
script, ext = os.path.splitext(script_ext)
sys.path.append(path)

module = importlib.import_module(script)
# importlib.reload(module)
