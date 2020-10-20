import subprocess

def execute_command(command_arr):
    result = subprocess.Popen(command_arr, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    text = result.communicate()[0]
    returncode = result.returncode
    return text, returncode
