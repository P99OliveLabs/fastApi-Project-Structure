from fastapi import FastAPI
import logging

from app.routes import users, finances, tenant, tenant_user#, tenant_user

app = FastAPI()
logging.basicConfig(level=logging.DEBUG)

# Include the routers from user and finance routes
app.include_router(users.router, prefix="/user", tags=["User"])
app.include_router(finances.router, prefix="/finance", tags=["Finance"])
app.include_router(tenant.router, prefix="/tenant", tags=["Tenant"])
app.include_router(tenant_user.router, prefix="/tenant_user", tags=["Tenant User"])
#app.include_router(tenant_user.router, prefix="/tenant_user", tags=["User"])

@app.get("/")
async def read_root():
    logging.info("Request received for root")
    return {"message": "Welcome to the FastAPI application!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
