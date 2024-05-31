from services import api_gateway_service
from services.DTO import logs_dto
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
            api_gateway_service.send_logs(objectSuspect)

        print("running check temp: ", datetime.now())
    except Exception as e:
        api_gateway_service.send_logs(
            logs_dto.Logs(str(e), Type.agentError, SubType.temp, "", "")
        )

def verify_tTemp_suspects():
    # TODO: Implementar verificação dos temp
    return False, logs_dto.Logs("", Type.suspectLog, SubType.temp, "", "")