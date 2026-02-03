from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .. import schemas, hashing, models


def create_user(request: schemas.User, db: Session):
    new_user = models.User(
        name=request.name,
        email=request.email,
        password=hashing.Hash.hash_password(request.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def get_user(id: int, db: Session):
    user = db.get(models.User, id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found"
        )
    return user
