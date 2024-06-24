import os, requests
from services import cognito_service
from services.DTO import logs_dto

def send_logs(log: logs_dto.Logs):
    API_GATEWAY_URL = os.getenv("API_GATEWAY_URL")
    
    data = log.toJson()
    
    headers = {'Content-type': 'application/json', 'Authorization': 'Bearer '+cognito_service.get_token()}
        
    response = requests.post(API_GATEWAY_URL, data=data, headers=headers)
    
    return response.json()
    
