from fastapi import FastAPI
from routes.postRoute import postRouter
from routes.hpRoute import hpRouter
from config.db import engine, Base

app = FastAPI()
app.include_router(postRouter)
app.include_router(hpRouter)


@app.on_event("startup")
async def startup():
    # create db table
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)

# GET operation at route '/'


@app.get('/')
async def root_api():
    return {"message": "Welcome to posts API"}
