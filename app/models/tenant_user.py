# app/models/tenant_user.py

from pydantic import BaseModel
from typing import Optional

# Tenant-User relationship model
class TenantUser(BaseModel):
    id: int
    tenant_id: int  # Foreign key to Tenant
    name: str       # User name
    email: str      # User email
    role: Optional[str] = "member"  # Role can be 'admin', 'member', etc.

    class Config:
        orm_mode = True

# Model for creating Tenant-User relationship
class TenantUserCreate(BaseModel):
    tenant_id: int
    name: str
    email: str
    role: Optional[str] = "member"

# Model for updating Tenant-User relationship
class TenantUserUpdate(BaseModel):
    role: Optional[str] = "member"
