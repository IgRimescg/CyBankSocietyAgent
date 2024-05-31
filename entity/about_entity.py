from datetime import datetime

class about():
    name: str
    version: str
    lastCheck: datetime


    def __init__(self, name:str, version: str):
        self.name = name
        self.version = version
        self.last_check = datetime.now()
        
    def toSave(self):
        return {"name": self.name, "version": self.version, "last_check": self.last_check.strftime('%d/%m/%Y %H:%M:%S')}
