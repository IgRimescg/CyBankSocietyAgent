import threading
from services import api_gateway_service
from services.DTO import logs_dto
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
            api_gateway_service.send_logs(objectSuspect)

        print("running check logs: ", datetime.now())
    except Exception as e:
        api_gateway_service.send_logs(
            logs_dto.Logs(str(e), Type.agentError, SubType.logs, "", "")
        )


def verify_logs_suspects():
    # TODO: Implementar verificação dos logs
    return False, logs_dto.Logs("", Type.suspectLog, SubType.logs, "", "")