from services import api_gateway_service
from services.DTO import logs_dto
from datetime import datetime
from enums.LogSubType import SubType
from enums.LogType import Type
import threading

def start():
    thread = threading.Thread(target=start_sharings_check)
    thread.start()

def start_sharings_check():
    try:
        suspectLog, objectSuspect = verify_sharings_suspects()
        if(suspectLog):
            api_gateway_service.send_logs(objectSuspect)

        print("running check sharings:", datetime.now())
    except Exception as e:
        api_gateway_service.send_logs(
            logs_dto.Logs(str(e), Type.agentError, SubType.sharings, "", "")
        )  

def verify_sharings_suspects():
    # TODO: Implementar verificação dos sharings
    return False, logs_dto.Logs("", Type.suspectLog , SubType.sharings, "", "")