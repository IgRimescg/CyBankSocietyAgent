
import time
from timeloop import Timeloop
from datetime import timedelta
from services import aboutService
from datetime import datetime

tl = Timeloop()

@tl.job(interval=timedelta(minutes=5))
def sample_job_every_2s():
    aboutService.updateAboutLastCheck(datetime.now())
    print("5 minutes job current time : {}".format(time.ctime()))
    


def start():
    tl.start(block=False)