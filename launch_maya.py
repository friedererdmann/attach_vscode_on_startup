import os
import inspect
import subprocess


def get_maya_path():
    return r"C:\\Program Files\\Autodesk\\Maya2022\\bin\\maya.exe"


def get_current_path():
    current_file = os.path.abspath(inspect.getsourcefile(get_current_path))
    path, _ = os.path.split(current_file)
    return path


def get_environment():
    env = os.environ.copy()
    env['PYTHONPATH'] = os.path.join(get_current_path(), 'scripts')
    return env


process = subprocess.Popen([get_maya_path(),], env=get_environment())
if process: process.wait()
