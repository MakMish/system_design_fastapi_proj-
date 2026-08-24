from fastapi import FastAPI
from src.user.routes import router as user_router
from src.utils.dbconn import engine,Base
import logging
app=FastAPI()
import logging
async def db_init():
     async with engine.begin() as conn:
          await conn.run_sync(Base.metadata.create_all)
logging.basicConfig(
    level=logging.INFO,  # important
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
app.include_router(user_router)

async def init_db():
     async with engine.begin() as conn:
          await conn.run_sync(Base.metadata.create_all)

@app.on_event("startup")
async def onstartup():
     await init_db()
     