# app/services/tenant_user_service.py

from fastapi import HTTPException, status
from app.database.demo_database.fake_tenant_user_db import FakeTenantUserDBAdapter  # or RealTenantUserDBAdapter
from app.models.tenant_user import TenantUser, TenantUserCreate, TenantUserUpdate
from typing import List, Optional
from app.constants import TENANT_USER_CREATION_FAILED, TENANT_USER_UPDATE_FAILED, TENANT_USER_DELETION_FAILED, TENANT_USER_NOT_FOUND

# Instantiate the appropriate adapter
tenant_user_db_adapter = FakeTenantUserDBAdapter()  # Replace with RealTenantUserDBAdapter(db) for real DB

async def get_all_tenant_users() -> List[Optional[TenantUser]]:
    return await tenant_user_db_adapter.get_all_tenant_users()

async def get_tenant_user_by_id(tenant_user_id: int) -> Optional[TenantUser]:
    tenant_user = await tenant_user_db_adapter.get_tenant_user_by_id(tenant_user_id)
    if not tenant_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=TENANT_USER_NOT_FOUND)
    return tenant_user

async def add_tenant_user(tenant_user: TenantUserCreate) -> Optional[TenantUser]:
    return await tenant_user_db_adapter.add_tenant_user(tenant_user)

async def update_tenant_user(tenant_user_id: int, tenant_user: TenantUserUpdate) -> Optional[TenantUser]:
    return await tenant_user_db_adapter.update_tenant_user(tenant_user_id, tenant_user)

async def delete_tenant_user(tenant_user_id: int) -> bool:
    return await tenant_user_db_adapter.delete_tenant_user(tenant_user_id)
