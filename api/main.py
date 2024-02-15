import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.routes import item, file, directory

load_dotenv()

app = FastAPI()
allowed_origins = os.getenv('ALLOWED_ORIGINS', '').split(',')


app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(item.router)
app.include_router(file.router)
app.include_router(directory.router)
