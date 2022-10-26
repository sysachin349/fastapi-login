from urllib.request import Request
from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

import JWTtoken

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# def get_current_user(token:str=Depends(oauth2_scheme)):

#     print(f"token: {token}")
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )


#     return JWTtoken.verifyToken(token,credentials_exception)

# def get_current_user(request: Request):
#     # print(request.cookies.get("user"))
#     user = request.cookies.get("user")
#     if not user:
#         return False
#     else:
#         return True

def get_current_user(request):
    return (request.cookies.get("user"))