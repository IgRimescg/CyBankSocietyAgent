from datetime import datetime

class token_cognito():
    access_token: str
    expires_in: int
    token_type: str
    object_type: str


    def __init__(self, access_token:str, expires_in: int, token_type: str):
        self.access_token = access_token
        self.expires_in = expires_in
        self.token_type = token_type
        self.object_type = "COGNITO_TOKEN"
        
    def to_save(self):
        return {"access_token": self.access_token, "expires_in": self.expires_in, "token_type": self.token_type, "object_type": self.object_type}
