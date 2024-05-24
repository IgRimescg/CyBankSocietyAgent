from services import ApiGatewayService
from services.DTO import SuspectLogsDTO

def start():
    suspectLog, objectSuspect = verifyUsersSuspects()
    if(suspectLog):
        ApiGatewayService.sendSuspectLogs(objectSuspect)

    print("running check users")

def verifyUsersSuspects():
    # TODO: Implementar verificação dos users
    return False, SuspectLogsDTO.SuspectLogs("","","","")