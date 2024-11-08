from typing import List, Optional
from app.models.user import User, UserCreate, UserUpdate

# Interface for the database adapter
class UserDatabaseAdapter:
    async def get_all_users(self) -> List[User]:
        raise NotImplementedError

    async def get_user_by_id(self, user_id: int) -> Optional[User]:
        raise NotImplementedError

    async def add_user(self, user: UserCreate) -> User:
        raise NotImplementedError

    async def update_user(self, user_id: int, user: UserUpdate) -> Optional[User]:
        raise NotImplementedError

    async def delete_user(self, user_id: int) -> bool:
        raise NotImplementedError
