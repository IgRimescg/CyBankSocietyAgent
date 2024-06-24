
import time
from timeloop import Timeloop
from datetime import timedelta
from services import about_service
from datetime import datetime
from core import start_checks

tl = Timeloop()

@tl.job(interval=timedelta(seconds=10))
def checkEvery5s():
    StartChecks.startCheck()
    AboutService.updateAboutLastCheck(datetime.now())
    print("5 minutes job current time : {}".format(time.ctime()))
    


def start():
    tl.start(block=False)