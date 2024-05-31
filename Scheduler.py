
import time
from timeloop import Timeloop
from datetime import timedelta
from services import about_service
from datetime import datetime
from core import start_checks

tl = Timeloop()

@tl.job(interval=timedelta(minutes=1))
def check_every_5s():
    start_checks.star_check()
    about_service.update_about_last_check(datetime.now())
    print("5 minutes job current time : {}".format(time.ctime()))
    


def start():
    tl.start(block=False)