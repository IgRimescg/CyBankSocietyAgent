from datetime import datetime

class SuspectLogs():
    description: str
    type: str
    namespace: str
    ip: str
    timeCheck: datetime
    
    def __init__(self, description:str, type:str, namespace: str, ip: str):
        self.description = description
        self.type = type
        self.namespace = namespace
        self.ip = ip
        self.timeCheck = datetime.now()
        
    def toJson(self):
        return {"description": self.description, "type": self.type, "namespace": self.namespace, "ip": self.ip, "timeCheck": self.timeCheck.strftime('%d/%m/%Y %H:%M:%S')}