# app/services/user_service.py

from fastapi import HTTPException, status
from app.database.demo_database.fake_user_db import FakeUserDBAdapter  # or RealUserDBAdapter
from app.models.user import User, UserCreate, UserUpdate
from typing import List, Optional
from app.constants import USER_BLACKLISTED_MESSAGE

from app.services.security.blacklist import is_user_blacklisted

# Instantiate the appropriate adapter
user_db_adapter = FakeUserDBAdapter()  # Replace with RealUserDBAdapter(db) for real DB

async def get_all_users() -> List[Optional[User]]:
    return await user_db_adapter.get_all_users()

async def get_user_by_id(user_id: int) -> Optional[User]:
    # Fetch the user from the database using the adapter
    user = await user_db_adapter.get_user_by_id(user_id)

    # If user is not found, return None (handling 'User not found' in the route instead)
    if not user:
        return None

    # Extract the user's id and check their status (e.g., blacklist check)
    blacklisted = await is_user_blacklisted(user.id)
    if blacklisted:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=USER_BLACKLISTED_MESSAGE.format(user_id=user.id))

    return user

async def add_user(user: UserCreate) -> Optional[User]:
    return await user_db_adapter.add_user(user)

async def update_user(user_id: int, user: UserUpdate) -> Optional[User]:
    return await user_db_adapter.update_user(user_id, user)

async def delete_user(user_id: int) -> bool:
    return await user_db_adapter.delete_user(user_id)
