from typing import Optional, List

from datetime import datetime, timezone
from app.backend.Schemas import UserCreateSchema, UserPublicSchema, RoleEnum

from fastapi import APIRouter, HTTPException, status, Depends, Query
from fastapi.encoders import jsonable_encoder

from motor.motor_asyncio import AsyncIOMotorClient
from motor.motor_asyncio import AsyncIOMotorCollection
from http import HTTPStatus

router = APIRouter(prefix="/users", tags=["users"])

MONGO_DETAILS = "mongodb://database-mongodb:27017"  # Usando o nome do container na rede Docker
client = AsyncIOMotorClient(MONGO_DETAILS)
database = client["database"]
users_collection = database.get_collection("Users")


async def is_user_exist(email: str, users_collection: AsyncIOMotorCollection):
    """Verifica se um usuário com o e-mail informado já existe no banco de dados."""
    if await users_collection.find_one({"email": email}):
        raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail="E-mail já cadastrado"
            )

@router.post("/", response_description="User created", status_code=HTTPStatus.CREATED)
async def create_user(user: UserCreateSchema):
    await is_user_exist(user.email, users_collection)

    # Converte o objeto pydantic para um dicionário compatível com MongoDB
    user_data = jsonable_encoder(user)
    # Adiciona o campo created_at com o horário atual
    user_data["created_at"] = datetime.now(timezone.utc)
    # Insere o usuário na coleção "Users"
    new_user = await users_collection.insert_one(user_data)
    if not new_user.inserted_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Erro ao criar usuário"
        )
    # Retorna o id do usuário criado
    return {"id": str(new_user.inserted_id)}


@router.get("/", response_description="Users retrieved", response_model=List[UserPublicSchema])
async def get_users(email: Optional[str] = Query(None, description="E-mail do usuário a ser procurado"),
                    role: Optional[RoleEnum] = Query(None, description="Role do usuário a ser procurado")):
    query = {}
    if email:
        query["email"] = email
    if role:
        query["role"] = role
    users = await users_collection.find(query).to_list()
    if not users:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Nenhum usuário encontrado")
    return users