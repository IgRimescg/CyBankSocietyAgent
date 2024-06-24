import os, requests, json
from entity import token_cognito_entity
from repository import cognito_repository
from services import jwt_decode_service

def generate_token():
    COGNITO_URL = os.getenv("COGNITO_URL")
    COGNITO_SCOPE = os.getenv("COGNITO_SCOPE")
    COG_CLIENT_ID = os.getenv("CLIENT_ID")
    COG_CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    
    data = {
        'grant_type' : 'client_credentials',
        'scope' : COGNITO_SCOPE,
        'client_id' : COG_CLIENT_ID,
        'client_secret' : COG_CLIENT_SECRET
    }
    
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
        
    response = requests.post(COGNITO_URL, data=data, headers=headers)
    
    object = convert_to_object(response.json())
    
    cognito_repository.saveToken(object)
    
def get_token():
    token = cognito_repository.getToken()
    if token is None or jwt_decode_service.verify_token_expire(token=token):
        generate_token()
        get_token()    
    
    return token

def convert_to_object(object):
    return token_cognito_entity.TokenCognito(object['access_token'], object['expires_in'], object['token_type'])