from fastapi import FastAPI

from routers import auth, users

app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)


@app.get('/')
def read_root():
    """returns a hello world message"""
    return {'message': 'Hello world! Im a root!'}
