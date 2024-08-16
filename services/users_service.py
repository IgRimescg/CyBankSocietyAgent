from repository import users_repository
from datetime import datetime

def start_users():
    users_repository.start_users()

def check_different_users_equals(users):
    different_users = []
    db_users = users_repository.get_users()
    for user in users:
        if not check_user_exist_db(db_users, user):
            different_users.append(user)
    
    return different_users        

def check_user_exist_db(db_users, user):
    for db_user in db_users:
        if user == db_user:
            return True
    return False

def insert_new_user(user: str):
    users_repository.insert_new_user(user)
