from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from router import router
from random import randint
import uvicorn

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # Список разрешенных источников
    allow_credentials=True, # Разрешить отправку куки и авторизационных заголовков
    allow_methods=["*"], # Разрешить все HTTP методы (GET, POST, PUT, DELETE и т.д.)
    allow_headers=["*"], # Разрешить все заголовки в запросах
)

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True, port=3000)