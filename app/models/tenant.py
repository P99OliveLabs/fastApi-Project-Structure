from pydantic import BaseModel

class Tenant(BaseModel):
    id: int
    name: str
    domain: str  # Changed 'email' to 'domain' as it is more relevant for tenants

# Model for tenant creation (input data)
class TenantCreate(BaseModel):
    name: str
    domain: str

class TenantUpdate(BaseModel):
    name: str
    domain: str
