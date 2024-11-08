from typing import List, Optional
from app.models.user import User, UserCreate, UserUpdate
from app.database.demo_database.database import UserDatabaseAdapter

# Sample in-memory database
FAKE_USER_DB = [
    User(id=1, name="Alice", email="alice@example.com"),
    User(id=2, name="Bob", email="bob@example.com"),
    User(id=3, name="Charlie", email="charlie@example.com")  # This will be the blacklisted user
]

class FakeUserDBAdapter(UserDatabaseAdapter):
    async def get_all_users(self) -> List[User]:
        return FAKE_USER_DB

    async def get_user_by_id(self, user_id: int) -> Optional[User]:
        for user in FAKE_USER_DB:
            if user.id == user_id:
                return user
        return None

    async def add_user(self, user: UserCreate) -> User:
        new_id = len(FAKE_USER_DB) + 1
        new_user = User(id=new_id, **user.dict())
        FAKE_USER_DB.append(new_user)
        return new_user

    async def update_user(self, user_id: int, user: UserUpdate) -> Optional[User]:
        for index, existing_user in enumerate(FAKE_USER_DB):
            if existing_user.id == user_id:
                updated_user = User(id=user_id, **user.dict())
                FAKE_USER_DB[index] = updated_user
                return updated_user
        return None

    async def delete_user(self, user_id: int) -> bool:
        for index, existing_user in enumerate(FAKE_USER_DB):
            if existing_user.id == user_id:
                FAKE_USER_DB.pop(index)
                return True
        return False
