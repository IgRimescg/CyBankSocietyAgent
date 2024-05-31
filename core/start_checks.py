from core.cronjobs import start_check_cronjobs
from core.downloads import start_check_downloads
from core.logs import start_check_logs
from core.sharings import start_check_sharings
from core.temp import start_check_temp
from core.users import start_check_users


def star_check():
    print("Start batch of checks")
    start_check_cronjobs.start()
    start_check_downloads.start()
    start_check_logs.start()
    start_check_sharings.start()
    start_check_temp.start()
    start_check_users.start()
    print("Finish batch of checks")