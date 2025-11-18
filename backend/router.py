from fastapi import APIRouter
from random import randint
from forms import UserForm

router = APIRouter(
    prefix='/api'
)

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

