from datetime import datetime

class About():
    name: str
    version: str
    lastCheck: datetime


    def __init__(self, name:str, version: str):
        self.name = name
        self.version = version
        self.lastCheck = datetime.now()
        
    def toSave(self):
        return {"name": self.name, "version": self.version, "lastCheck": self.lastCheck.strftime('%d/%m/%Y %H:%M:%S')}
