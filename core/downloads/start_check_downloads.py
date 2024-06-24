import threading
from services import api_gateway_service
from services.DTO import logs_dto
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
            api_gateway_service.send_logs(objectSuspect)

        print("running check downloads: ", datetime.now())
    except Exception as e:
        api_gateway_service.send_logs(
            logs_dto.Logs(str(e), Type.agentError, SubType.download, "", "")
        )


def verify_downloads_suspects():
    # TODO: Implementar verificação dos downloads
    return False, logs_dto.Logs("", Type.suspectLog, SubType.download, "", "")