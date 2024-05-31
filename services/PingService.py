import subprocess

def check_internet_connect():
    try:
        subprocess.check_output(['ping', '-c', '1', '8.8.8.8'])
        return True
    except subprocess.CalledProcessError:
        return False