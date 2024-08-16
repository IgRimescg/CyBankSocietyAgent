from services import api_gateway_service, users_service
from services.DTO import logs_dto
from datetime import datetime
from enums.LogSubType import SubType
from enums.LogType import Type
import threading
import os, subprocess

def start():
    thread = threading.Thread(target=start_users_check)
    thread.start() 

def start_users_check():
    try:
        suspectLog, objectSuspect = verify_users_suspects()
        if(suspectLog):
            api_gateway_service.send_logs(objectSuspect)
        print("running check users: ", datetime.now())
    except Exception as e:
        api_gateway_service.send_logs(
            logs_dto.Logs(str(e), Type.agentError, SubType.users, "", "")
        )


def verify_users_suspects():
    command_out = subprocess.run("dscl . list /Users", shell=True, stdout=subprocess.PIPE, text=True, encoding="cp437")
    results = command_out.stdout.split("\n")

    clean_results = clean_users(results)

    users_not_in_db = users_service.check_different_users_equals(clean_results)

    for new_user in users_not_in_db:
        users_service.insert_new_user(new_user)

    str_users_not_in_db = ", ".join(map(str, users_not_in_db))

    if len(users_not_in_db) > 0:
        return True, logs_dto.Logs(f"Detected new users in device executed: {str_users_not_in_db}", Type.suspectLog, SubType.cronjob, "", "")        
    
    
    return False, logs_dto.Logs("", Type.suspectLog, SubType.users, "", "")

def clean_users(results):
    all_users = []

    for result in results:    
        if result.startswith("_") or result == "":
            continue
        all_users.append(result)

    return all_users