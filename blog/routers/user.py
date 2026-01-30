from fastapi import APIRouter
from fastapi import Depends, status, HTTPException
from .. import database, hashing, schemas, models
from sqlalchemy.orm import Session



router = APIRouter(
    tags=['Users']
)

@router.post('/user', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db : Session = Depends(database.get_db)):
    new_user = models.User(name=request.name, email=request.email, password=hashing.Hash.hash_password(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get('/user/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(database.get_db)):
    user = db.query(models.User).get(id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'User with id {id} not found')
    return user
