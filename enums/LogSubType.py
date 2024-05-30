from enum import Enum

class SubType(Enum):
    cronjob = 'CRONJOB',
    download = 'DOWNLOAD',
    logs = 'LOGS',
    sharings = 'SHARINGS',
    temp = 'TEMP',
    users = 'USERS'