import enum

from sqlalchemy import (
    Boolean,
    Column,
    Date,
    DateTime,
    Integer,
    String,
    Text,
    func,
    Enum,
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Role(enum.Enum):
    admin: str = "admin"  # type: ignore
    moderator: str = "moderator"  # type: ignore
    user: str = "user"  # type: ignore


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username: str | Column[str] = Column(String(150), nullable=False)
    email: str | Column[str] = Column(String(150), nullable=False, unique=True)
    password: str | Column[str] = Column(String(255), nullable=False)
    refresh_token: str | Column[str] | None = Column(String(255), nullable=True)
    avatar: str | Column[str] | None = Column(String(255), nullable=True)
    role: Enum | Column[Enum] = Column("roles", Enum(Role), default=Role.user)


class Contact(Base):
    """
    Ім'я
    Прізвище
    Електронна адреса
    Номер телефону
    День народження
    Додаткові дані (необов'язково)
    """

    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone = Column(String)
    birthday = Column(Date)
    comments = Column(Text)
    favorite = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
