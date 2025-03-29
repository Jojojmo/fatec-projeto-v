from datetime import datetime
from enum import Enum
from typing import Optional

from bson import ObjectId
from fastapi import APIRouter, HTTPException, status
from fastapi.encoders import jsonable_encoder
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel, EmailStr, Field
from http import HTTPStatus

class Message(BaseModel):
    message: str




class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema, handler):
        json_schema = handler(core_schema)
        json_schema.update(type="string")
        return json_schema


# Schema e Enum do usuário com todos os campos (interno)
class RoleEnum(str, Enum):
    professor = "professor"
    aluno = "aluno"


# Schema para criação do usuário (não inclui id, created_at e outros gerenciados pelo sistema)
class UserCreateSchema(BaseModel):
    name: str
    email: EmailStr
    password: str
    role: RoleEnum

    class Config:
        json_schema_extra = {
            "example": {
                "name": "João Silva",
                "email": "joao.silva@example.com",
                "password": "senha_segura",
                "role": "aluno",
            }
        }


class UserSchema(UserCreateSchema):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    role: RoleEnum


    class Config:
        validate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        json_schema_extra = {
            "example": {
                "_id": "60d0fe4f5311236168a109ca",
                "name": "João Silva",
                "email": "joao.silva@example.com",
                "password": "senha_segura",
                "created_at": "2025-03-28T12:34:56Z",
                "role": "aluno",
            }
        }


# Schema público (não retorna informações sensíveis, como id e password)
class UserPublicSchema(BaseModel):
    name: str
    email: EmailStr
    created_at: datetime
    role: RoleEnum

    class Config:
        json_schema_extra = {
            "example": {
                "name": "João Silva",
                "email": "joao.silva@example.com",
                "created_at": "2025-03-28T12:34:56Z",
                "role": "aluno",
            }
        }