from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ProdutoQueryParams(BaseModel):
    limit: int = Field(10, le=100)
    offset: int = Field(0)
    order_by: str = Field('id')
    order_direction: str = Field('asc')
    nome: Optional[str] = Field(None, min_length=1)
    categoria_id: Optional[int] = Field(None)


class ProdutoBaseSchema(BaseModel):
    nome: str
    descricao: str
    cor: str
    preco: float
    categoria_id: int


class ProdutoCreateSchema(ProdutoBaseSchema): ...


class ProdutoDB(ProdutoBaseSchema):
    id: int
    criado_em: datetime
    atualizado_em: datetime
    preco_com_desconto: Optional[float] = None


class ProdutoLista(BaseModel):
    produtos: list[ProdutoDB]
