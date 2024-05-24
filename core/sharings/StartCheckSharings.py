from services import ApiGatewayService
from services.DTO import SuspectLogsDTO

def start():
    suspectLog, objectSuspect = verifySharingsSuspects()
    if(suspectLog):
        ApiGatewayService.sendSuspectLogs(objectSuspect)

    print("running check sharings")

def verifySharingsSuspects():
    # TODO: Implementar verificação dos sharings
    return False, SuspectLogsDTO.SuspectLogs();