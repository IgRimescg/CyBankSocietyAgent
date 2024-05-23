from datetime import datetime

class TokenCognito():
    accessToken: str
    expiresIn: int
    tokenType: str
    objectType: str


    def __init__(self, accessToken:str, expiresIn: int, tokenType: str):
        self.accessToken = accessToken
        self.expiresIn = expiresIn
        self.tokenType = tokenType
        self.objectType = "COGNITO_TOKEN"
        
    def toSave(self):
        return {"accessToken": self.accessToken, "expiresIn": self.expiresIn, "tokenType": self.tokenType, "objectType": self.objectType};
