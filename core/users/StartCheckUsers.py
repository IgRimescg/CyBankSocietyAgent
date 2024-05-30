from services import ApiGatewayService
from services.DTO import LogsDTO
from datetime import datetime
from enums.LogSubType import SubType
from enums.LogType import Type
import threading

def start():
    thread = threading.Thread(target=startUsersCheck)
    thread.start() 

def startUsersCheck():
    suspectLog, objectSuspect = verifyUsersSuspects()
    if(suspectLog):
        ApiGatewayService.sendSuspectLogs(objectSuspect)

    print("running check users: ", datetime.now())


def verifyUsersSuspects():
    # TODO: Implementar verificação dos users
    return False, LogsDTO.Logs("", Type.suspectLog, SubType.users, "", "")