from core.cronjobs import StartCheckCronjobs
from core.downloads import StartCheckDownloads
from core.logs import StartCheckLogs
from core.sharings import StartCheckSharings
from core.temp import StartCheckTemp
from core.users import StartCheckUsers


def startCheck():
    print("Start batch of checks")
    StartCheckCronjobs.start()
    StartCheckDownloads.start()
    StartCheckLogs.start()
    StartCheckSharings.start()
    StartCheckTemp.start()
    StartCheckUsers.start()
    print("Finish batch of checks")