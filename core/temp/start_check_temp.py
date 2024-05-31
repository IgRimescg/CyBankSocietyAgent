from services import ApiGatewayService
from services.DTO import LogsDTO
from datetime import datetime
from enums.LogSubType import SubType
from enums.LogType import Type
import threading

def start():
    thread = threading.Thread(target=start_temp_check)
    thread.start()
    

def start_temp_check():
    try:
        suspectLog, objectSuspect = verify_tTemp_suspects()
        if(suspectLog):
            ApiGatewayService.send_logs(objectSuspect)

        print("running check temp: ", datetime.now())
    except Exception as e:
        ApiGatewayService.send_logs(
            LogsDTO.Logs(str(e), Type.agentError, SubType.temp, "", "")
        )

def verify_tTemp_suspects():
    # TODO: Implementar verificação dos temp
    return False, LogsDTO.Logs("", Type.suspectLog, SubType.temp, "", "")