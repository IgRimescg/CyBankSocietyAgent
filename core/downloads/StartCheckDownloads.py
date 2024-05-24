from services import ApiGatewayService
from services.DTO import SuspectLogsDTO

def start():
    suspectLog, objectSuspect = verifyDownloadsSuspects()
    if(suspectLog):
        ApiGatewayService.sendSuspectLogs(objectSuspect)

    print("running check downloads")

def verifyDownloadsSuspects():
    # TODO: Implementar verificação dos downloads
    return False, SuspectLogsDTO.SuspectLogs("","","","")