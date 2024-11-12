# app/services/tenant_service.py

from fastapi import HTTPException, status
from app.database.demo_database.fake_tenant_db import FakeTenantDBAdapter  # or RealTenantDBAdapter
from app.models.tenant import Tenant, TenantCreate, TenantUpdate
from typing import List, Optional
from app.constants import TENANT_BLACKLISTED_MESSAGE

# Instantiate the appropriate adapter
tenant_db_adapter = FakeTenantDBAdapter()  # Replace with RealTenantDBAdapter(db) for real DB

async def get_all_tenants() -> List[Optional[Tenant]]:
    return await tenant_db_adapter.get_all_tenants()

async def get_tenant_by_id(tenant_id: int) -> Optional[Tenant]:
    # Fetch the tenant from the database using the adapter
    tenant = await tenant_db_adapter.get_tenant_by_id(tenant_id)

    # If tenant is not found, return None (handling 'Tenant not found' in the route instead)
    if not tenant:
        return None

    # Extract the tenant's id and check their status (e.g., blacklist check)
    blacklisted = await is_tenant_blacklisted(tenant.id)
    if blacklisted:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=TENANT_BLACKLISTED_MESSAGE.format(tenant_id=tenant.id))

    return tenant

async def add_tenant(tenant: TenantCreate) -> Optional[Tenant]:
    return await tenant_db_adapter.add_tenant(tenant)

async def update_tenant(tenant_id: int, tenant: TenantUpdate) -> Optional[Tenant]:
    return await tenant_db_adapter.update_tenant(tenant_id, tenant)

async def delete_tenant(tenant_id: int) -> bool:
    return await tenant_db_adapter.delete_tenant(tenant_id)
