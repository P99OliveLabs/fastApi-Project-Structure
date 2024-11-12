from typing import List, Optional
from app.models.user import User, UserCreate, UserUpdate
from app.models.tenant import Tenant, TenantCreate, TenantUpdate
from app.models.tenant_user import TenantUser, TenantUserCreate, TenantUserUpdate

# Interface for user-related database operations
class UserDatabaseAdapter:
    async def get_all_users(self, tenant_id: Optional[int] = None) -> List[User]:
        """Fetch all users, optionally filtered by tenant."""
        raise NotImplementedError

    async def get_user_by_id(self, user_id: int, tenant_id: Optional[int] = None) -> Optional[User]:
        """Fetch a user by ID, optionally within the context of a specific tenant."""
        raise NotImplementedError

    async def add_user(self, user: UserCreate, tenant_id: int) -> User:
        """Add a user under a specific tenant."""
        raise NotImplementedError

    async def update_user(self, user_id: int, user: UserUpdate, tenant_id: Optional[int] = None) -> Optional[User]:
        """Update a user under a specific tenant."""
        raise NotImplementedError

    async def delete_user(self, user_id: int, tenant_id: Optional[int] = None) -> bool:
        """Delete a user under a specific tenant."""
        raise NotImplementedError

# Interface for tenant-related database operations
class TenantDatabaseAdapter:
    async def get_all_tenants(self) -> List[Tenant]:
        """Fetch all tenants."""
        raise NotImplementedError

    async def get_tenant_by_id(self, tenant_id: int) -> Optional[Tenant]:
        """Fetch a tenant by ID."""
        raise NotImplementedError

    async def add_tenant(self, tenant: TenantCreate) -> Tenant:
        """Add a new tenant."""
        raise NotImplementedError

    async def update_tenant(self, tenant_id: int, tenant: TenantUpdate) -> Optional[Tenant]:
        """Update an existing tenant."""
        raise NotImplementedError

    async def delete_tenant(self, tenant_id: int) -> bool:
        """Delete a tenant."""
        raise NotImplementedError

class TenantUserDatabaseAdapter:
    async def get_all_tenant_users(self) -> List[TenantUser]:
        """Fetch all tenant users."""
        raise NotImplementedError

    async def get_tenant_user_by_id(self, tenant_user_id: int) -> Optional[TenantUser]:
        """Fetch a tenant user by ID."""
        raise NotImplementedError

    async def add_tenant_user(self, tenant_user: TenantUserCreate) -> TenantUser:
        """Add a new tenant-user relationship."""
        raise NotImplementedError

    async def update_tenant_user(self, tenant_user_id: int, tenant_user: TenantUserUpdate) -> Optional[TenantUser]:
        """Update an existing tenant-user relationship."""
        raise NotImplementedError

    async def delete_tenant_user(self, tenant_user_id: int) -> bool:
        """Delete a tenant-user relationship."""
        raise NotImplementedError