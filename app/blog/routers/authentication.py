from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from .. import database, models, JWToken
from ..hashing import Hash
from fastapi import HTTPException
from sqlalchemy.orm import Session

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/login")
def Login(
    request: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(database.get_db),
):
    user = db.query(models.User).filter(models.User.name == request.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not Hash.verify_password(request.password, user.password):
        raise HTTPException(status_code=404, detail="Incorrect password")

    access_token = JWToken.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
