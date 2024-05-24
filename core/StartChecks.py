from cronjobs import StartCheckCronjobs
from downloads import StartCheckDownloads
from logs import StartCheckLogs
from sharings import StartCheckSharings
from temp import StartCheckTemp
from users import StartCheckUsers


def startCheck():
    StartCheckCronjobs.start()
    StartCheckDownloads.start()
    StartCheckLogs.start()
    StartCheckSharings.start()
    StartCheckTemp.start()
    StartCheckUsers.start()