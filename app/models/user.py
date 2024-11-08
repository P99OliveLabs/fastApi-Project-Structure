from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str

# Model for user creation (input data)
class UserCreate(BaseModel):
    name: str
    email: str

class UserUpdate(BaseModel):
    name: str
    email: str