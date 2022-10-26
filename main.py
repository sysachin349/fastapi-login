from fastapi.responses import RedirectResponse
from urllib import request
from fastapi_login import LoginManager
from fastapi import FastAPI,Depends,HTTPException,Request,Response,File,UploadFile
import starlette.status as status
from schemas import users, loginInfo, profile
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import models,JWTtoken
from models import Base, user
from database import SessionLocal,engine
from sqlalchemy.orm import Session
from hashing import hash
import auth2
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordBearer
import uuid
import playwright
from playwright.async_api import async_playwright



user_data={}

app = FastAPI()

#this is to mount static files and to load html files
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# this is to create database connections and creating tables inside databases
Base.metadata.create_all(bind=engine)



SECRET=JWTtoken.SECRET_KEY

manager=LoginManager(SECRET,token_url='/auth/login',use_cookie=True)
manager.cookie_name= 'admin'

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/sign-up',tags=['sign-up'])
def signup(request:users,db:Session=Depends(get_db)):
   create_user=models.user(userName=request.userName,Email=request.Email,Password=hash.bcrypt(request.Password))
   db.add(create_user)
   db.commit()
   db.refresh(create_user)
   return create_user


@app.get('/login',tags=['Login'])
def login(request:Request):
    return templates.TemplateResponse('index.html', {"request":request})




@app.post('/login', tags=['Login'])
async def login(request:Request, db:Session=Depends(get_db)):
    print('*********************** you are here!')
    user_data = dict(await request.form())
    user=db.query(models.user).filter(models.user.Email==user_data['username']).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'The user does not exits')
    if not hash.verify_password(user_data['password'],user.Password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'incorrect Password!')
    #access_token=manager.create_access_token(data={"sub":user.Email})
    response = RedirectResponse('/applications', status_code=status.HTTP_302_FOUND)
    response.set_cookie(key="user", value=user.Email)
    return response



@app.get('/applications',tags=['Applications'])
async def blog(request:Request):
    logged_user=auth2.get_current_user(request)
    if not logged_user:
        return RedirectResponse('/login')
    else:
        return templates.TemplateResponse('applications.html', {"request":request})



@app.post("/uploadfiles/",tags=['upload files'])
async def create_upload_files(request:Request,files:UploadFile,db:Session=Depends(get_db)):
    logged_user=auth2.get_current_user(request)
    if not logged_user:
        return RedirectResponse('/login')
    else:
        user_data = dict(await request.form())
        profile=str(uuid.uuid1()).replace('-','')[0:15]
        print(user_data)
        for i in files.file.read().decode('utf-8').split()[1:]:
            createData=models.profile(profileID=profile,FirstName=i.split(',')[0],LastName=i.split(',')[1],Email=i.split(',')[2].strip(),Password=i.split(',')[3].strip(),Recoverymail=i.split(',')[4],Gender=i.split(',')[5],PhoneNo=i.split(',')[6],Month=i.split(',')[7],Date=i.split(',')[8],Year=i.split(',')[9],proxyIP=i.split(',')[10],Port=i.split(',')[11])
            db.add(createData)
            db.commit()
            db.refresh(createData)
            #return RedirectResponse('/notSpam')

@app.post('/notSpam',tags=['notSpam'])
async def notSpam(request:Request,db:Session=Depends(get_db)):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("http://playwright.dev")
