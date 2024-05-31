from services import ApiGatewayService
from services.DTO import LogsDTO
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
            ApiGatewayService.send_logs(objectSuspect)

        print("running check sharings:", datetime.now())
    except Exception as e:
        ApiGatewayService.send_logs(
            LogsDTO.Logs(str(e), Type.agentError, SubType.sharings, "", "")
        )  

def verify_sharings_suspects():
    # TODO: Implementar verificação dos sharings
    return False, LogsDTO.Logs("", Type.suspectLog , SubType.sharings, "", "")