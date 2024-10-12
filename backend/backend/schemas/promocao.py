from datetime import datetime

from pydantic import BaseModel


class PromocaoBaseSchema(BaseModel):
    porcentagem_desconto: float
    categoria_id: int


class PromocaoCreateSchema(PromocaoBaseSchema): ...


class PromocaoDB(PromocaoBaseSchema):
    id: int
    criado_em: datetime
    atualizado_em: datetime


class PromocaoLista(BaseModel):
    promocoes: list[PromocaoDB]
