from services import ApiGatewayService
from services.DTO import LogsDTO
import threading
from datetime import datetime
from enums.LogSubType import SubType
from enums.LogType import Type
import os, subprocess
from datetime import timedelta



def start():
    thread = threading.Thread(target=startCronjobCheck)
    thread.start()
    
def startCronjobCheck():
    suspectLog, objectSuspect = verifyCronjobSuspects()
    if(suspectLog):
        ApiGatewayService.sendSuspectLogs(objectSuspect)

    print("running check cronjobs: ", datetime.now())
    

def verifyCronjobSuspects():
    suspect_commands = ["chmod", "sudo", "crontab", "wget", "rm -rf"]

    now = datetime.now()
    now_minus = now - timedelta(seconds=10)
    
    command_out = subprocess.run('cat ~/.zsh_history', shell=True, stdout=subprocess.PIPE, text=True, encoding="cp437")
    results = command_out.stdout.split("\n")
   
    for result in results:
        command_separation = result.split(";")

        if len(command_separation) >= 2:   
            timestamp = getDateTime(command_separation)
            if timestamp >= now_minus:
                command = getCommand(command_separation)
                if check_suspect_commnad(command, suspect_commands):
                    return True, LogsDTO.Logs(f"Detected suspect command executed: {command}", Type.suspectLog, SubType.cronjob, "", "")
            
    
    return False, LogsDTO.Logs("", Type.suspectLog, SubType.cronjob, "", "")

def check_suspect_commnad(command, suspect_commands):
    for suspect_command in suspect_commands:
        if suspect_command in command:
            return True
    return False

def getDateTime(command_separation):
    timestamp_raw = command_separation[0]
    start = ':'
    end = ':'
    timepstamp = timestamp_raw[timestamp_raw.find(start)+len(start):timestamp_raw.rfind(end)]
    return datetime.fromtimestamp(int(timepstamp))

def getCommand(command_separation):
    return command_separation[1]