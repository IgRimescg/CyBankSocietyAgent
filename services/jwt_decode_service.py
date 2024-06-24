import jwt
import time

def verify_token_expire(token: str):
    decoded = jwt.decode(token, options={"verify_signature": False})
    
    return time.time() >= decoded['exp']
    