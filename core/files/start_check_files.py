from services import api_gateway_service
from services.DTO import logs_dto
from datetime import datetime
from enums.LogSubType import SubType
from enums.LogType import Type
import threading

def start():
    thread = threading.Thread(target=start_files_check)
    thread.start()

def start_files_check():
    try:
        suspectLog, objectSuspect = verify_files_suspects()
        if(suspectLog):
            api_gateway_service.send_logs(objectSuspect)

        print("running check files:", datetime.now())
    except Exception as e:
        api_gateway_service.send_logs(
            logs_dto.Logs(str(e), Type.agentError, SubType.files, "", "")
        )  

def verify_files_suspects():
   #pode remover/mudar/adicionar de acordo com a necessidade 
    suspect_paths = ['/etc', '/usr/local/bin', '/Library', '~/Library', '/Users/Shared', '/private/tmp']  # paths a serem monitorados
    suspect_file_extensions = ['.sh', '.pl']  # extensões, talvez incluir tambem .app e/ou .pkg?
    suspect_file_mod_times = time.time() - 86400  # Arquivos modificados nos ultimos x segundos

    suspect_logs = []
    for path in suspect_paths:
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                if any(file.endswith(ext) for ext in suspect_file_extensions):
                    if os.path.getmtime(file_path) > suspect_file_mod_times:
                        suspect_logs.append(f"Suspicious file detected: {file_path}")

    if suspect_logs:
        log_message = "\n".join(suspect_logs)
        return True, logs_dto.Logs(log_message, Type.suspectLog, SubType.files, "", "")
    else:
        return False, logs_dto.Logs("", Type.suspectLog, SubType.files, "", "")
