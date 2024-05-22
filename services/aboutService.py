from repository import aboutRepository
from datetime import datetime

def startAbout():
    aboutRepository.startAbout()
    
def updateAboutLastCheck(dateTime: datetime):
    aboutRepository.updateAboutLastCheck(dateTime);