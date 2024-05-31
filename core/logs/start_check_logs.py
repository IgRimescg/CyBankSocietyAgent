import threading
from services import ApiGatewayService
from services.DTO import LogsDTO
from datetime import datetime
from enums.LogSubType import SubType
from enums.LogType import Type

def start():
    thread = threading.Thread(target=start_logs_check)
    thread.start()
    

def start_logs_check():
    try:
        suspectLog, objectSuspect = verify_logs_suspects()
        if(suspectLog):
            ApiGatewayService.send_logs(objectSuspect)

        print("running check logs: ", datetime.now())
    except Exception as e:
        ApiGatewayService.send_logs(
            LogsDTO.Logs(str(e), Type.agentError, SubType.logs, "", "")
        )


def verify_logs_suspects():
    # TODO: Implementar verificação dos logs
    return False, LogsDTO.Logs("", Type.suspectLog, SubType.logs, "", "")