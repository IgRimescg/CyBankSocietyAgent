import os
from tinydb import TinyDB, Query
from entity import token_cognito_entity


db = TinyDB(os.getenv("DB_NAME"))
db_search = Query()


def get_token():
    
    find = db.search(db_search.object_type == 'COGNITO_TOKEN')
    
    if(len(find) > 0):
        return find[0]['access_token']
    
def save_token(token_entity: token_cognito_entity.token_cognito):
    delete_token()
    db.insert(token_entity.to_save())
    
def delete_token():
    db.remove(db_search.object_type == 'COGNITO_TOKEN')