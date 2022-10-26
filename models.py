import string
from xmlrpc.client import boolean
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base

class user(Base):
    __tablename__= 'user'
    id = Column(Integer,primary_key=True,index=True)
    userName = Column(String)
    Email = Column(String)
    Password = Column(String)


class profile(Base):
    __tablename__ = 'profile'
    SrNo = Column(Integer,primary_key=True,index=True)
    profileID = Column(String)
    FirstName = Column(String)
    LastName = Column(String)
    Email = Column(String)
    Password = Column(String)
    Recoverymail = Column(String)
    Gender = Column(String)
    PhoneNo =Column(Integer)
    Month = Column(Integer)
    Date = Column(Integer)
    Year = Column(Integer)
    proxyIP = Column(Integer)
    Port = Column(Integer)

