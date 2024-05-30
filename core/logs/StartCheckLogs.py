import threading
from services import ApiGatewayService
from services.DTO import LogsDTO
from datetime import datetime
from enums.LogSubType import SubType
from enums.LogType import Type

def start():
    thread = threading.Thread(target=startLogsCheck)
    thread.start()
    

def startLogsCheck():
    suspectLog, objectSuspect = verifyLogsSuspects()
    if(suspectLog):
        ApiGatewayService.sendSuspectLogs(objectSuspect)

    print("running check logs: ", datetime.now())


def verifyLogsSuspects():
    # TODO: Implementar verificação dos logs
    return False, LogsDTO.Logs("", Type.suspectLog, SubType.logs, "", "")