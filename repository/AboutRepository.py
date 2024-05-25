import os
from tinydb import TinyDB, Query
from entity import AboutEntity
from datetime import datetime

db = TinyDB(os.getenv("DB_NAME"))
db_search = Query()


def startAbout():
    about = AboutEntity.About('CyBank Society', '1.0.0')
    
    find = db.search(db_search.name == about.name)
    
    if(len(find) <= 0):
        db.insert(about.toSave())
    
def updateAboutLastCheck(dateTime: datetime):
    db.update({"lastCheck": dateTime.strftime('%d/%m/%Y %H:%M:%S')}, db_search.name == 'CyBank Society')
    
def getAbout():
    name = 'CyBank Society'
    find = db.search(db_search.name == name)
        
    if(len(find) > 0):
        return find[0]
    