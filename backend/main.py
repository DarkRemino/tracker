from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5173'],
    allow_credentials=True,
    allow_methods='*',
    allow_headers='*'
)

class LoginRequest(BaseModel):
    username: Optional[str]
    password: Optional[str]

fake_users_db = {
    'testuser': {
        'username': 'testuser',
        'password': 'password123'
    }
}

@app.post('/login')
async def login(request: LoginRequest):
    user = fake_users_db.get(request.username)

    if not user or user.password != request.password:
        raise HTTPException(status_code=401, detail='Invalid username or password!')

    return {'message': 'Login usccessful', 'username': user['username']}

