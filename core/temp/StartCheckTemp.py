from services import ApiGatewayService
from services.DTO import LogsDTO
from datetime import datetime
from enums.LogSubType import SubType
from enums.LogType import Type
import threading

def start():
    thread = threading.Thread(target=startTempCheck)
    thread.start()
    

def startTempCheck():
    suspectLog, objectSuspect = verifyTempSuspects()
    if(suspectLog):
        ApiGatewayService.sendSuspectLogs(objectSuspect)

    print("running check temp: ", datetime.now())

def verifyTempSuspects():
    # TODO: Implementar verificação dos temp
    return False, LogsDTO.Logs("", Type.suspectLog, SubType.temp, "", "")