import os, requests
from services import CognitoService
from services.DTO import LogsDTO

def sendSuspectLogs(suspectLog: LogsDTO.Logs):
    API_GATEWAY_URL = os.getenv("API_GATEWAY_URL")
    
    data = suspectLog.toJson()
    
    headers = {'Content-type': 'application/json', 'Authorization': 'Bearer '+CognitoService.getToken()}
        
    response = requests.post(API_GATEWAY_URL, data=data, headers=headers)
    
    return response.json()
    
