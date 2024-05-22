from repository import AboutRepository
from datetime import datetime

def startAbout():
    AboutRepository.startAbout()
    
def updateAboutLastCheck(dateTime: datetime):
    AboutRepository.updateAboutLastCheck(dateTime);