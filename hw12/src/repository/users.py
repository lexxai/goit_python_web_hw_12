from libgravatar import Gravatar
from sqlalchemy.orm import Session
from src.shemas.users import UserModel

from src.database.models import User


async def create_user(body: UserModel, db: Session) -> User | None:
    try:
        g = Gravatar(body.email)
        new_user = User(**body.model_dump(), avatar = g.get_image())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except Exception:
        return None
    return new_user


async def get_user_by_email(email: str | None, db: Session) -> User | None:
    if email:
        try:
            return db.query(User).filter_by(email=email).first()
        except Exception:
            ...
    return None


async def get_user_by_name(username: str | None, db: Session) -> User | None:
    if username:
        try:
            return db.query(User).filter_by(email=username).first()
        except Exception:
            ...
    return None


async def update_user_refresh_token(
    user: User, refresh_token: str | None, db: Session
) -> str | None:
    if user:
        try:
            user.refresh_token = refresh_token
            db.commit()
            return refresh_token
        except Exception:
            ...
    return None


async def update_by_name_refresh_token(
    username: str | None, refresh_token: str | None, db: Session
) -> str | None:
    if username and refresh_token:
        try:
            user = await get_user_by_name(username, db)
            return await update_user_refresh_token(user, refresh_token, db)
        except Exception:
            ...
    return None
