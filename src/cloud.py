import cloudinary
import redis
import httpx
from fastapi.requests import Request
import cloudinary.uploader
from fastapi.responses import JSONResponse
from src.utils.dbconn import Setting
from fastapi import File,HTTPException
r=redis.from_url(Setting().redis_url)
cloudinary.config(
  cloud_name=Setting().cloud_name,
  api_secret=Setting().cloud_api_secret,
  api_key=Setting().cloud_API_key,
  secure=True   
   )
async def img(request:Request,file1:File):
    count=r.incr(f"{request.client.host}:img")
    if count> 5:
        return JSONResponse(
            status_code=440,
            content={
                "status":"limit_exceeded"
            }
        )
    if count==1:
        r.expire(f"{request.client.host}:img",60)
        # async with httpx.AsyncClient() as client:
        #     await client.post()
    if file1.size<2*1024*1024:
        result=cloudinary.uploader.upload(file1.file)
        v=r.incr(f"{request.client.host}:img")
        print(v)
        if v==1:
            r.expire(f"{request.client.host}:img",60)
        return JSONResponse(
            status_code=201,
            content={
                "url":result.get("url")
            }
        )
    if file1.content_type.startwith("video"):
        raise HTTPException(status_code=400,detail="not a required file type")
    raise HTTPException(status_code=400,detail="ile size is more than 2mb")
    
    