# app/routes/user_route.py

from fastapi import APIRouter, HTTPException, status
from typing import List
from app.models.user import User, UserCreate, UserUpdate
from app.services.user_service import get_all_users, add_user, update_user, delete_user, get_user_by_id
from app.constants import NO_USERS_FOUND,USER_CREATION_FAILED, USER_UPDATE_FAILED, USER_DELETION_FAILED, USER_NOT_FOUND

router = APIRouter()

@router.get("/", response_model=List[User])
async def get_users():
    """Fetch all users from the database."""
    users = await get_all_users()
    if not users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=NO_USERS_FOUND)
    return users

@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int):
    """
    Fetch a user by ID, with checks for blacklisting status.
    """
    user = await get_user_by_id(user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )

    return user

@router.post("/", response_model=User, status_code=201)
async def create_user(user: UserCreate):
    """Create a new user in the database."""
    created_user = await add_user(user)
    if not created_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=USER_CREATION_FAILED)
    return created_user

@router.put("/{user_id}", response_model=User)
async def update_user_route(user_id: int, user: UserUpdate):
    """Update an existing user in the database."""
    updated_user = await update_user(user_id, user)
    if not updated_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=USER_UPDATE_FAILED)
    return updated_user

@router.delete("/{user_id}", status_code=204)
async def delete_user_route(user_id: int):
    """Delete a user from the database."""
    deleted = await delete_user(user_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=USER_DELETION_FAILED)
    return {"message": "User deleted successfully"}
