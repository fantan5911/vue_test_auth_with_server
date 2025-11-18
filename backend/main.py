from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from random import randint
import uvicorn

app = FastAPI()

router = APIRouter(
    prefix='/api'
)

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

class UserForm(BaseModel):
    email: str
    nickname: str
    password: str

users = []

UserID = randint(1, 8399499959)

@router.get("/users")
def get_users():
    return users

@router.post("/users")
def post_user(req: UserForm):
    global UserID

    newUser = {
        "id": UserID,
        "email": req.email,
        "nickname": req.nickname,
        "password": req.password
    }
    UserID = randint(1, 8399499959)
    users.append(newUser)

    return users

@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    global users
    initial_len = len(users)
    
    users = [user for user in users if user["id"] != user_id]
    
    if len(users) < initial_len:
        print(f"User with ID {user_id} deleted.")
        return {"message": f"User with ID {user_id} deleted successfully."}


app.include_router(router)

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True, port=3000)