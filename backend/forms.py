from pydantic import BaseModel

class UserForm(BaseModel):
    email: str
    nickname: str
    password: str