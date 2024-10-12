from datetime import datetime

from pydantic import BaseModel


class CategoriaBaseSchema(BaseModel):
    nome: str


class CategoriaCreateSchema(CategoriaBaseSchema): ...


class CategoriaDB(CategoriaBaseSchema):
    id: int
    criado_em: datetime
    atualizado_em: datetime

    class Config:
        from_attributes = True


class CategoriaLista(BaseModel):
    categorias: list[CategoriaDB]
