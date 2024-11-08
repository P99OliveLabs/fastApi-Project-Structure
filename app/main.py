from fastapi import FastAPI

from app.routes import users, finances

app = FastAPI()

# Include the routers from user and finance routes
app.include_router(users.router, prefix="/user", tags=["User"])
app.include_router(finances.router, prefix="/finance", tags=["Finance"])

@app.get("/")
async def read_root():
    return {"message": "Welcome to the FastAPI application!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
