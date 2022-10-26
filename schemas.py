from pydantic import BaseModel,EmailStr
from typing import Optional

class users(BaseModel):
    userName: str
    Email: EmailStr
    Password: str

class loginInfo(BaseModel):
    Email: EmailStr
    Password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    Email: Optional[str] = None

class profile(BaseModel):
    profileID: str
    FirstName: str
    LastName: str
    Email: str
    Password: str
    Recoverymail: str
    Gender: str
    PhoneNo: str
    Month: str
    Date: str
    Year: str