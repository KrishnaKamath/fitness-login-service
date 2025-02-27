from fastapi import FastAPI
from .auth import router as auth_router


# Initialize FastAPI app
app = FastAPI()

# Include the auth router
app.include_router(auth_router, prefix="/auth")

# You can include other routers here as your application grows
# from .some_other_module import some_other_router
# app.include_router(some_other_router, prefix="/some_other_prefix")

app.get("/")
def read_root():
    return {"message": "Welcome to the Fitness Tracker API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)