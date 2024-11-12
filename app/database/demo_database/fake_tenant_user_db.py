# app/database/demo_database/fake_tenant_user_db.py

from typing import List, Optional
from app.models.tenant_user import TenantUser, TenantUserCreate, TenantUserUpdate
from app.database.demo_database.database import TenantUserDatabaseAdapter
from app.database.demo_database.fake_tenant_db import FAKE_TENANT_DB  # Import tenants from the fake database

# Sample in-memory database for tenant-user relationships
FAKE_TENANT_USER_DB = [
    TenantUser(id=1, tenant_id=1, name="Alice", email="alice@example.com", role="business_analyst"),
    TenantUser(id=2, tenant_id=1, name="Bob", email="bob@example.com", role="storage_admin"),
    TenantUser(id=3, tenant_id=1, name="Carol", email="carol@example.com", role="business_consumer"),
    TenantUser(id=4, tenant_id=2, name="David", email="david@example.com", role="business_analyst"),
    TenantUser(id=5, tenant_id=2, name="Eve", email="eve@example.com", role="storage_admin"),
    TenantUser(id=6, tenant_id=2, name="Frank", email="frank@example.com", role="business_consumer"),
    TenantUser(id=7, tenant_id=3, name="Grace", email="grace@example.com", role="business_analyst"),
    TenantUser(id=8, tenant_id=3, name="Hank", email="hank@example.com", role="storage_admin"),
    TenantUser(id=9, tenant_id=3, name="Ivy", email="ivy@example.com", role="business_consumer"),
]

class FakeTenantUserDBAdapter(TenantUserDatabaseAdapter):
    async def get_all_tenant_users(self) -> List[TenantUser]:
        return FAKE_TENANT_USER_DB

    async def get_tenant_user_by_id(self, tenant_user_id: int) -> Optional[TenantUser]:
        for tenant_user in FAKE_TENANT_USER_DB:
            if tenant_user.id == tenant_user_id:
                return tenant_user
        return None

    async def add_tenant_user(self, tenant_user: TenantUserCreate) -> TenantUser:
        new_id = len(FAKE_TENANT_USER_DB) + 1
        new_tenant_user = TenantUser(id=new_id, **tenant_user.dict())
        FAKE_TENANT_USER_DB.append(new_tenant_user)
        return new_tenant_user

    async def update_tenant_user(self, tenant_user_id: int, tenant_user: TenantUserUpdate) -> Optional[TenantUser]:
        for index, existing_tenant_user in enumerate(FAKE_TENANT_USER_DB):
            if existing_tenant_user.id == tenant_user_id:
                updated_tenant_user = TenantUser(id=tenant_user_id, **tenant_user.dict())
                FAKE_TENANT_USER_DB[index] = updated_tenant_user
                return updated_tenant_user
        return None

    async def delete_tenant_user(self, tenant_user_id: int) -> bool:
        for index, existing_tenant_user in enumerate(FAKE_TENANT_USER_DB):
            if existing_tenant_user.id == tenant_user_id:
                FAKE_TENANT_USER_DB.pop(index)
                return True
        return False
