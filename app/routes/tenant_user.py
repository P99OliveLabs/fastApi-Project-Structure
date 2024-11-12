# app/routes/tenant_user.py

from fastapi import APIRouter, HTTPException, status
from typing import List
from app.models.tenant_user import TenantUser, TenantUserCreate, TenantUserUpdate
from app.services.tenant_user_service import get_all_tenant_users, add_tenant_user, update_tenant_user, delete_tenant_user, get_tenant_user_by_id
from app.constants import TENANT_USER_CREATION_FAILED, TENANT_USER_UPDATE_FAILED, TENANT_USER_DELETION_FAILED, TENANT_USER_NOT_FOUND

router = APIRouter()

@router.get("/", response_model=List[TenantUser])
async def get_tenant_users():
    """Fetch all tenant-user relationships."""
    tenant_users = await get_all_tenant_users()
    if not tenant_users:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No tenant-user relationships found")
    return tenant_users

@router.get("/{tenant_user_id}", response_model=TenantUser)
async def get_tenant_user(tenant_user_id: int):
    """Fetch a specific tenant-user relationship by ID."""
    tenant_user = await get_tenant_user_by_id(tenant_user_id)
    if not tenant_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=TENANT_USER_NOT_FOUND)
    return tenant_user

@router.post("/", response_model=TenantUser, status_code=201)
async def create_tenant_user(tenant_user: TenantUserCreate):
    """Create a new tenant-user relationship."""
    created_tenant_user = await add_tenant_user(tenant_user)
    if not created_tenant_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=TENANT_USER_CREATION_FAILED)
    return created_tenant_user

@router.put("/{tenant_user_id}", response_model=TenantUser)
async def update_tenant_user_route(tenant_user_id: int, tenant_user: TenantUserUpdate):
    """Update an existing tenant-user relationship."""
    updated_tenant_user = await update_tenant_user(tenant_user_id, tenant_user)
    if not updated_tenant_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=TENANT_USER_UPDATE_FAILED)
    return updated_tenant_user

@router.delete("/{tenant_user_id}", status_code=204)
async def delete_tenant_user_route(tenant_user_id: int):
    """Delete a tenant-user relationship."""
    deleted = await delete_tenant_user(tenant_user_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=TENANT_USER_DELETION_FAILED)
    return {"message": "Tenant-User relationship deleted successfully"}
