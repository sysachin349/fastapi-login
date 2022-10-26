from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException

from datetime import datetime, timedelta
import sys
sys.path.insert(0,'./env/lib/python3.9/site-packages')
from jose import jwt, JWTError
import schemas



SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


manager = LoginManager(SECRET_KEY, token_url='/login', use_cookie=True)

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verifyToken(token:str,credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        Email: str = payload.get("sub")
        if Email is None:
            raise credentials_exception
        token_data = schemas.TokenData(Email=Email)
    except JWTError:
        raise credentials_exception