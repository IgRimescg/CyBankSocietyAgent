from enum import Enum

class SubType(Enum):
    cronjob = 'CRONJOB',
    download = 'DOWNLOAD',
    logs = 'LOGS',
    connected_devices = 'CONNECTED_DEVICES',
    temp = 'TEMP',
    users = 'USERS',
    files = 'FILES'