import os, requests
from services import CognitoService
from services.DTO import LogsDTO

def send_logs(log: LogsDTO.Logs):
    API_GATEWAY_URL = os.getenv("API_GATEWAY_URL")
    
    data = log.toJson()
    
    headers = {'Content-type': 'application/json', 'Authorization': 'Bearer '+CognitoService.getToken()}
        
    response = requests.post(API_GATEWAY_URL, data=data, headers=headers)
    
    return response.json()
    
