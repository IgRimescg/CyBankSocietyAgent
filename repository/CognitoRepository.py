import os
from tinydb import TinyDB, Query
from entity import TokenCognitoEntity


db = TinyDB(os.getenv("DB_NAME"))
db_search = Query()


def getToken():
    
    find = db.search(db_search.objectType == 'COGNITO_TOKEN')
    
    if(len(find) > 0):
        return find[0]['accessToken']
    
def saveToken(tokenEntity: TokenCognitoEntity.TokenCognito):
    deleteToken()
    db.insert(tokenEntity.toSave())
    
def deleteToken():
    db.remove(db_search.objectType == 'COGNITO_TOKEN')