from passlib.context import CryptContext
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta
from jose import jwt

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

#####
pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

def hash_password(password: str) -> str: 
    return pwd_context.hash(password)

def verify_password(plain_password: str , hashed_password: str) -> bool:
    return pwd_context.verify(plain_password,hashed_password)
#####

########
def create_access_token(data:dict, expires_delta: timedelta = timedelta(minutes=30)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded_jwt
########