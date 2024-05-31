from services import ApiGatewayService
from services.DTO import LogsDTO
from datetime import datetime
from enums.LogSubType import SubType
from enums.LogType import Type
import threading

def start():
    thread = threading.Thread(target=start_users_check)
    thread.start() 

def start_users_check():
    try:
        suspectLog, objectSuspect = verify_users_suspects()
        if(suspectLog):
            ApiGatewayService.send_logs(objectSuspect)

        print("running check users: ", datetime.now())
    except Exception as e:
        ApiGatewayService.send_logs(
            LogsDTO.Logs(str(e), Type.agentError, SubType.users, "", "")
        )


def verify_users_suspects():
    # TODO: Implementar verificação dos users
    return False, LogsDTO.Logs("", Type.suspectLog, SubType.users, "", "")