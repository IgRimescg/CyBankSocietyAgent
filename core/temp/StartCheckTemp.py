from services import ApiGatewayService
from services.DTO import SuspectLogsDTO

def start():
    suspectLog, objectSuspect = verifyTempSuspects()
    if(suspectLog):
        ApiGatewayService.sendSuspectLogs(objectSuspect)

    print("running check temp")

def verifyTempSuspects():
    # TODO: Implementar verificação dos temp
    return False, SuspectLogsDTO.SuspectLogs("","","","")