# app/routes/tenant_route.py

from fastapi import APIRouter, HTTPException, status
from typing import List
from app.models.tenant import Tenant, TenantCreate, TenantUpdate
from app.services.tenant_service import get_all_tenants, add_tenant, update_tenant, delete_tenant, get_tenant_by_id
from app.constants import NO_TENANTS_FOUND, TENANT_CREATION_FAILED, TENANT_UPDATE_FAILED, TENANT_DELETION_FAILED, TENANT_NOT_FOUND

router = APIRouter()

@router.get("/", response_model=List[Tenant])
async def get_tenants():
    """Fetch all tenants from the database."""
    tenants = await get_all_tenants()
    if not tenants:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=NO_TENANTS_FOUND)
    return tenants

@router.get("/{tenant_id}", response_model=Tenant)
async def get_tenant(tenant_id: int):
    """Fetch a tenant by ID."""
    tenant = await get_tenant_by_id(tenant_id)

    if not tenant:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Tenant with id {tenant_id} not found"
        )

    return tenant

@router.post("/", response_model=Tenant, status_code=201)
async def create_tenant(tenant: TenantCreate):
    """Create a new tenant in the database."""
    created_tenant = await add_tenant(tenant)
    if not created_tenant:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=TENANT_CREATION_FAILED)
    return created_tenant

@router.put("/{tenant_id}", response_model=Tenant)
async def update_tenant_route(tenant_id: int, tenant: TenantUpdate):
    """Update an existing tenant in the database."""
    updated_tenant = await update_tenant(tenant_id, tenant)
    if not updated_tenant:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=TENANT_UPDATE_FAILED)
    return updated_tenant

@router.delete("/{tenant_id}", status_code=204)
async def delete_tenant_route(tenant_id: int):
    """Delete a tenant from the database."""
    deleted = await delete_tenant(tenant_id)
    if not deleted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=TENANT_DELETION_FAILED)
    return {"message": "Tenant deleted successfully"}
