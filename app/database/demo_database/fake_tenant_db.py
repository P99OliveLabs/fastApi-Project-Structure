from typing import List, Optional
from app.models.tenant import Tenant, TenantCreate, TenantUpdate
from app.database.demo_database.database import TenantDatabaseAdapter

# Sample in-memory database
FAKE_TENANT_DB = [
    Tenant(id=1, name="Tenant One", domain="tenant1.example.com"),
    Tenant(id=2, name="Tenant Two", domain="tenant2.example.com"),
    Tenant(id=3, name="Tenant Three", domain="tenant3.example.com")  # This could represent a special status if needed
]

class FakeTenantDBAdapter(TenantDatabaseAdapter):
    async def get_all_tenants(self) -> List[Tenant]:
        return FAKE_TENANT_DB

    async def get_tenant_by_id(self, tenant_id: int) -> Optional[Tenant]:
        for tenant in FAKE_TENANT_DB:
            if tenant.id == tenant_id:
                return tenant
        return None

    async def add_tenant(self, tenant: TenantCreate) -> Tenant:
        new_id = len(FAKE_TENANT_DB) + 1
        new_tenant = Tenant(id=new_id, **tenant.dict())
        FAKE_TENANT_DB.append(new_tenant)
        return new_tenant

    async def update_tenant(self, tenant_id: int, tenant: TenantUpdate) -> Optional[Tenant]:
        for index, existing_tenant in enumerate(FAKE_TENANT_DB):
            if existing_tenant.id == tenant_id:
                updated_tenant = Tenant(id=tenant_id, **tenant.dict())
                FAKE_TENANT_DB[index] = updated_tenant
                return updated_tenant
        return None

    async def delete_tenant(self, tenant_id: int) -> bool:
        for index, existing_tenant in enumerate(FAKE_TENANT_DB):
            if existing_tenant.id == tenant_id:
                FAKE_TENANT_DB.pop(index)
                return True
        return False
