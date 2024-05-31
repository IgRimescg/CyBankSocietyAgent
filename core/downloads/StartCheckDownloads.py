import threading
from services import ApiGatewayService
from services.DTO import LogsDTO
from datetime import datetime
from enums.LogSubType import SubType
from enums.LogType import Type

def start():
    thread = threading.Thread(target=start_downloads_check)
    thread.start()
    

def start_downloads_check():
    try:
        suspectLog, objectSuspect = verify_downloads_suspects()
        if(suspectLog):
            ApiGatewayService.send_logs(objectSuspect)

        print("running check downloads: ", datetime.now())
    except Exception as e:
        ApiGatewayService.send_logs(
            LogsDTO.Logs(str(e), Type.agentError, SubType.download, "", "")
        )


def verify_downloads_suspects():
    # TODO: Implementar verificação dos downloads
    return False, LogsDTO.Logs("", Type.suspectLog, SubType.download, "", "")