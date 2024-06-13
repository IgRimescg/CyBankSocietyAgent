from core.cronjobs import start_check_cronjobs
from core.downloads import start_check_downloads
from core.logs import start_check_logs
from core.connected_devices import start_check_connected_devices
from core.temp import start_check_temp
from core.users import start_check_users
from core.files import start_check_files
from services import ping_service


def star_check():
    print("Start batch of checks")

    if(ping_service.check_internet_connect()):
        start_check_cronjobs.start()
        start_check_downloads.start()
        start_check_logs.start()
        start_check_connected_devices.start()
        start_check_temp.start()
        start_check_users.start()
        start_check_files.start()
        
    print("Finish batch of checks")