from datetime import datetime
from typing import Any, Optional, Annotated

from fastapi import Form
from pydantic import BaseModel, Field, EmailStr


from .owner import OwnerResponse


class CatModel(BaseModel):
    nickname: str = Field("Lukas", min_length=3, max_length=16)
    age: int = Field(1, ge=0, le=30)
    description: str
    vaccinated: bool = False
    owner_id: int = Field(1, gt=0)


class CatVactinatedModel(BaseModel):
    vaccinated: bool = False


class CatResponse(BaseModel):
    id: int
    nickname: str
    age: int
    description: str
    vaccinated: bool
    owner: OwnerResponse

    class Config:
        from_attributes = True
