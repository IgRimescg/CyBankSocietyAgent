from services import ApiGatewayService
from services.DTO import LogsDTO
import threading
from datetime import datetime
from enums.LogSubType import SubType
from enums.LogType import Type

def start():
    thread = threading.Thread(target=startCronjobCheck)
    thread.start()
    
def startCronjobCheck():
    suspectLog, objectSuspect = verifyCronjobSuspects()
    if(suspectLog):
        ApiGatewayService.sendSuspectLogs(objectSuspect)

    print("running check cronjobs: ", datetime.now())
    

def verifyCronjobSuspects():
    # TODO: Implementar verificação dos cronjobs
    return False, LogsDTO.Logs("", Type.suspectLog, SubType.cronjob, "", "")