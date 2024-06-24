from services import api_gateway_service
from services.DTO import logs_dto
from datetime import datetime
from enums.LogSubType import SubType
from enums.LogType import Type
import threading

def start():
    thread = threading.Thread(target=start_connected_devices_check)
    thread.start()

def start_connected_devices_check():
    try:
        suspectLog, objectSuspect = verify_connected_devices_suspects()
        if(suspectLog):
            api_gateway_service.send_logs(objectSuspect)

        print("running check connected devices:", datetime.now())
    except Exception as e:
        api_gateway_service.send_logs(
            logs_dto.Logs(str(e), Type.agentError, SubType.connected_devices, "", "")
        )  

def verify_connected_devices_suspects():
    # TODO: Implementar verificação dos connected devices
    return False, logs_dto.Logs("", Type.suspectLog , SubType.connected_devices, "", "")