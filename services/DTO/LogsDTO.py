from datetime import datetime
from enums.LogSubType import SubType
from enums.LogType import Type

class Logs():
    description: str
    type: Type
    subType: SubType
    namespace: str
    ip: str
    timeCheck: datetime

    def __init__(self):
        print("init")
    
    def __init__(self, description:str, type:Type, subType:SubType, namespace: str, ip: str):
        self.description = description
        self.type = type
        self.subType = subType
        self.namespace = namespace
        self.ip = ip
        self.timeCheck = datetime.now()
        
    def toJson(self):
        return {"description": self.description, "type": self.type.value, "subType": self.subType.value, "namespace": self.namespace, "ip": self.ip, "timeCheck": self.timeCheck.strftime('%d/%m/%Y %H:%M:%S')}