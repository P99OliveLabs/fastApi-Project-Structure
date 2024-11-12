# app/constants.py

# User-related constants
USER_NOT_FOUND = "User not found"
USER_CREATION_FAILED = "Failed to create user"
USER_UPDATE_FAILED = "User not found or update failed"
USER_DELETION_FAILED = "User not found or deletion failed"
NO_USERS_FOUND = "No users found"
USER_BLACKLISTED_MESSAGE = "User {user_id} is blacklisted."

# Tenant-related constants
TENANT_NOT_FOUND = "Tenant not found"
TENANT_CREATION_FAILED = "Failed to create tenant"
TENANT_UPDATE_FAILED = "Tenant not found or update failed"
TENANT_DELETION_FAILED = "Tenant not found or deletion failed"
NO_TENANTS_FOUND = "No tenants found"
TENANT_BLACKLISTED_MESSAGE = "Tenant {tenant_id} is blacklisted."
TENANT_ALREADY_EXISTS = "Tenant with the specified details already exists"

# General constants for both user and tenant operations (if needed)
OPERATION_FORBIDDEN = "Operation not allowed"
INVALID_INPUT_PROVIDED = "Invalid input provided"

# Finance-related constants (from original)
NO_FINANCES_FOUND = "No financial records found"
FINANCE_CREATION_FAILED = "Finance record creation failed"

# Tenant User related constants
TENANT_USER_CREATION_FAILED = "Failed to create tenant user"
TENANT_USER_UPDATE_FAILED = "Tenant user not found or update failed"
TENANT_USER_DELETION_FAILED = "Tenant user not found or deletion failed"
TENANT_USER_NOT_FOUND = "Tenant user not found"