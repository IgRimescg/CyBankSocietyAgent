from services import ApiGatewayService
from services.DTO import SuspectLogsDTO

def start():
    suspectLog, objectSuspect = verifyCronjobSuspects()
    if(suspectLog):
        ApiGatewayService.sendSuspectLogs(objectSuspect)

    print("running check cronjobs")

def verifyCronjobSuspects():
    # TODO: Implementar verificação dos cronjobs
    return False, SuspectLogsDTO.SuspectLogs("","","","")