import jwt
import time

def verifyTokenExpire(token: str):
    decoded = jwt.decode(token, options={"verify_signature": False})
    
    return time.time() >= decoded['exp']
    