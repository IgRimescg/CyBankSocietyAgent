import os
from tinydb import TinyDB, Query
from entity import about_entity
from datetime import datetime
import os, subprocess

db = TinyDB(os.getenv("DB_NAME"))
db_search = Query()


def get_users():
    find = db.search(db_search.object_type == 'USERS')
    
    if(len(find) > 0):
        return find[0]['users']
    
def start_blank_users():
    db.insert({"object_type":"USERS", "users": []})
    
def insert_new_user(user: str):
    if user == "": return
    find = db.search(db_search.object_type == 'USERS')
    find[0]['users'].append(user)
    db.update({"users": find[0]['users']}, db_search.object_type == 'USERS')
    
def start_users():
    command_out = subprocess.run("dscl . list /Users", shell=True, stdout=subprocess.PIPE, text=True, encoding="cp437")
    results = command_out.stdout.split("\n")
    all_users = []

    for result in results:    
        if result.startswith("_"):
            continue
        all_users.append(result)
    
    find = db.search(db_search.object_type == 'USERS')
    
    if(len(find) <= 0):
        start_blank_users()
        for user in all_users:
            insert_new_user(user)

    