from repository import about_repository
from datetime import datetime

def start_about():
    about_repository.start_about()
    
def update_about_last_check(dateTime: datetime):
    about_repository.update_about_last_check(dateTime);
    
def get_about():
    return about_repository.get_about()