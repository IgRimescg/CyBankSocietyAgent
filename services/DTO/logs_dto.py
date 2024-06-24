from datetime import datetime
from enums.LogSubType import SubType
from enums.LogType import Type

class Logs():
    description: str
    type: Type
    sub_type: SubType
    namespace: str
    ip: str
    time_check: datetime

    def __init__(self):
        print("init")
    
    def __init__(self, description:str, type:Type, sub_type:SubType, namespace: str, ip: str):
        self.description = description
        self.type = type
        self.sub_type = sub_type
        self.namespace = namespace
        self.ip = ip
        self.time_check = datetime.now()
        
    def toJson(self):
        return {"description": self.description, "type": self.type.value, "sub_type": self.sub_type.value, "namespace": self.namespace, "ip": self.ip, "time_check": self.time_check.strftime('%d/%m/%Y %H:%M:%S')}