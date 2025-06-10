from typing import Annotated
from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.database import db_dependency
from app.schemas import CreateUserRequests, Token
from app.models import User
from .item import create_access_token, authenticate_user, get_current_user
from .config import bcrypt_context

auth_router = APIRouter(
    prefix = '/auth',
    tags=['auth']
)

user_dependency = Annotated[dict, Depends(get_current_user)]

@auth_router.post('/', status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, create_user_request: CreateUserRequests):
    create_user_model = User(
        username = create_user_request.username,
        hashed_password = bcrypt_context.hash(create_user_request.password)
    )
    db.add(create_user_model)
    db.commit()

@auth_router.post('/token', response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise  HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user')
    token = create_access_token(user.username, user.id, timedelta(minutes=20))

    return {'access_token': token, "token_type":"bearer"}