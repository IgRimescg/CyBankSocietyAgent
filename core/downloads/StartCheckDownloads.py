import threading
from services import ApiGatewayService
from services.DTO import LogsDTO
from datetime import datetime
from enums.LogSubType import SubType
from enums.LogType import Type

def start():
    thread = threading.Thread(target=startDownloadsCheck)
    thread.start()
    

def startDownloadsCheck():
    suspectLog, objectSuspect = verifyDownloadsSuspects()
    if(suspectLog):
        ApiGatewayService.sendSuspectLogs(objectSuspect)

    print("running check downloads: ", datetime.now())


def verifyDownloadsSuspects():
    # TODO: Implementar verificação dos downloads
    return False, LogsDTO.Logs("", Type.suspectLog, SubType.download, "", "")