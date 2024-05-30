from services import ApiGatewayService
from services.DTO import LogsDTO
from datetime import datetime
from enums.LogSubType import SubType
from enums.LogType import Type
import threading

def start():
    thread = threading.Thread(target=startSharingsCheck)
    thread.start()

def startSharingsCheck():
    suspectLog, objectSuspect = verifySharingsSuspects()
    if(suspectLog):
        ApiGatewayService.sendSuspectLogs(objectSuspect)

    print("running check sharings:", datetime.now())

def verifySharingsSuspects():
    # TODO: Implementar verificação dos sharings
    return False, LogsDTO.Logs("", Type.suspectLog , SubType.sharings, "", "")