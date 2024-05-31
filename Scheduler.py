
import time
from timeloop import Timeloop
from datetime import timedelta
from services import AboutService
from datetime import datetime
from core import start_checks

tl = Timeloop()

@tl.job(interval=timedelta(minutes=5))
def checkEvery5s():
    start_checks.start_check()
    AboutService.updateAboutLastCheck(datetime.now())
    print("5 minutes job current time : {}".format(time.ctime()))
    


def start():
    tl.start(block=False)