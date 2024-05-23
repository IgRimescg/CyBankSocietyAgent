import os, requests, json
from entity import TokenCognitoEntity
from repository import CognitoRepository

def generateToken():
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
    
    CognitoRepository.saveToken(object)
    
def getToken():
    token = CognitoRepository.getToken()
    if token is None:
        generateToken()
        getToken()
        
    return token

def convert_to_object(object):
    return TokenCognitoEntity.TokenCognito(object['access_token'], object['expires_in'], object['token_type'])