from services import ApiGatewayService
from services.DTO import SuspectLogsDTO

def start():
    suspectLog, objectSuspect = verifyLogsSuspects()
    if(suspectLog):
        ApiGatewayService.sendSuspectLogs(objectSuspect)

    print("running check logs")

def verifyLogsSuspects():
    # TODO: Implementar verificação dos logs
    return False, SuspectLogsDTO.SuspectLogs("","","","")