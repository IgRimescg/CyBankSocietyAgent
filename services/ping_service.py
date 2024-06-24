import subprocess

def check_internet_connect():
    return (lambda a: True if 0 == a.system('ping 192.168.0.1 -n 3 -l 32 -w 3 > clear') else False)(__import__('os'))