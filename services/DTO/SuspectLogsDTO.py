from datetime import datetime

class SuspectLogs():
    description: str
    type: str
    timeCheck: datetime
    
    def __init__(self, description:str, type: str):
        self.description = description
        self.type = type
        self.timeCheck = datetime.now()
        
    def toJson(self):
        return {"description": self.description, "type": self.type, "timeCheck": self.timeCheck.strftime('%d/%m/%Y %H:%M:%S')}