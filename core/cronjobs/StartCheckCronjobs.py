from services import ApiGatewayService
from services.DTO import LogsDTO
import threading
from datetime import datetime
from enums.LogSubType import SubType
from enums.LogType import Type

def start():
    thread = threading.Thread(target=start_cronjob_check)
    thread.start()
    
def start_cronjob_check():
    try:
        suspectLog, objectSuspect = verify_cronjob_suspects()
        if(suspectLog):
            ApiGatewayService.send_logs(objectSuspect)

        print("running check cronjobs: ", datetime.now())
    except Exception as e:
        ApiGatewayService.send_logs(
            LogsDTO.Logs(str(e), Type.agentError, SubType.cronjob, "", "")
        )
    

def verify_cronjob_suspects():
    # TODO: Implementar verificação dos cronjobs
    return False, LogsDTO.Logs("", Type.suspectLog, SubType.cronjob, "", "")