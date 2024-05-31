import os
from tinydb import TinyDB, Query
from entity import about_entity
from datetime import datetime

db = TinyDB(os.getenv("DB_NAME"))
db_search = Query()


def start_about():
    about = about_entity.about('CyBank Society', '1.0.0')
    
    find = db.search(db_search.name == about.name)
    
    if(len(find) <= 0):
        db.insert(about.toSave())
    
def update_about_last_check(dateTime: datetime):
    db.update({"last_check": dateTime.strftime('%d/%m/%Y %H:%M:%S')}, db_search.name == 'CyBank Society')
    
def get_about():
    name = 'CyBank Society'
    find = db.search(db_search.name == name)
        
    if(len(find) > 0):
        return find[0]
    