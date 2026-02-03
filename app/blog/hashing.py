from passlib.context import CryptContext
from typing import Any


class Hash:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @staticmethod
    def hash_password(password: str) -> str:
        return Hash.pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: Any) -> bool:
        # Convert to string if it's a SQLAlchemy Column
        if hasattr(hashed_password, "__class__") and "Column" in str(
            type(hashed_password)
        ):
            hashed_password = str(hashed_password)
        return Hash.pwd_context.verify(plain_password, hashed_password)
