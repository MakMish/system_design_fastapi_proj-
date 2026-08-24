from src.user.schema import impexp
import time
import logging
import redis
from fastapi.requests import Request
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends
from src.user.model import data
from sqlalchemy.ext.asyncio import AsyncSession
from src.utils.dbconn import get_db
from src.dbmodel import Setting
from sqlalchemy import select
from fastapi.responses import JSONResponse
from passlib.context import CryptContext
from src.user.user_auth import create_refresh_token,create_access_token
r=redis.from_url(Setting().redis_url)
logger=logging.getLogger(__name__)
pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")
async def all_data(db:AsyncSession=Depends(get_db)):
    result=await db.execute(select(impexp).offset(0).limit(10))
    data= result.scalars().all()
    if data is None:
        return JSONResponse(
            status_code=400,
            content={
                "status":"data not exists"
            }
        )
    else:
        return data

async def add_data(request:Request,data1:data ,db:AsyncSession):
    host = request.client.host
    key = f"{host}:register"

    count = r.incr(key)
    if count == 1:
        r.expire(key, 60)   
    if count > 5:
        return JSONResponse(
            status_code=429,  
            content={"status": "limit_exceeded_try_again"}
        )
    
    clean_password=data1.password.strip()
    token=await create_refresh_token({"email":data1.email})
    user=impexp(
        Name=data1.Name,
        email=data1.email,
        hash_password=pwd_context.hash(clean_password),
        reftok=token
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return JSONResponse(
        status_code=201,
        content={
            "status":"data added"
        }
    )

async def login(request: Request, data: OAuth2PasswordRequestForm, db1: AsyncSession):
    host = request.client.host
    key = f"{host}:login"

    count = r.incr(key)
    if count == 1:
        r.expire(key, 60)   
    if count > 5:
        return JSONResponse(
            status_code=429,  
            content={"status": "limit_exceeded"}
        )

    start1 = time.time()
    cache_key = f"{data.username}:{host}"
    cache = r.get(cache_key)

    if cache:
        end1 = time.time()
        logger.info(f"time from cache {end1 - start1}")
        print("from cache")

        return JSONResponse(
            status_code=200,
            content={"status": cache}
        )

    start = time.time()

    result = await db1.execute(
        select(impexp).where(impexp.email == data.username)
    )
    target = result.scalars().first()

    if not target:
        return JSONResponse(
            status_code=400,
            content={"status": "user doesn't exist, please register"}
        )

    
    if not pwd_context.verify(data.password, target.hash_password):
        return JSONResponse(
            status_code=400,
            content={"status": "password failure"}
        )

    token = await create_access_token(target.reftok, db=db1)
    r.setex(cache_key, 180, token)

    print("from database")
    end = time.time()
    logger.info(f"time from db is {end - start}")

    return JSONResponse(
        status_code=200,
        content={"status": f"acc token is {token}"}
    )