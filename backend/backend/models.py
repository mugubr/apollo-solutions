from datetime import datetime
from typing import Optional

from sqlalchemy import ForeignKey, func
from sqlalchemy.orm import Mapped, mapped_column, registry, relationship

table_registry = registry()


@table_registry.mapped_as_dataclass
class Produto:
    __tablename__ = 'produtos'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome: Mapped[str] = mapped_column(unique=True)
    descricao: Mapped[str]
    cor: Mapped[str]
    preco: Mapped[float]
    criado_em: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    atualizado_em: Mapped[datetime] = mapped_column(
        init=False, onupdate=func.now(), default=func.now()
    )

    categoria_id: Mapped[int] = mapped_column(ForeignKey('categorias.id'))

    categoria: Mapped['Categoria'] = relationship(
        'Categoria', back_populates='produtos'
    )

    @property
    def preco_com_desconto(self) -> float:
        if self.categoria.promocao:
            desconto = self.categoria.promocao.porcentagem_desconto
            return self.preco * (1 - desconto / 100)
        return self.preco


@table_registry.mapped_as_dataclass
class Categoria:
    __tablename__ = 'categorias'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)
    nome: Mapped[str] = mapped_column(unique=True)
    criado_em: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    atualizado_em: Mapped[datetime] = mapped_column(
        init=False, onupdate=func.now(), default=func.now()
    )

    produtos: Mapped[list['Produto']] = relationship(
        'Produto', back_populates='categoria', default_factory=list
    )

    promocao: Mapped[Optional['Promocao']] = relationship(
        'Promocao',
        back_populates='categoria',
        uselist=False,
        cascade='all, delete-orphan',
        default=None,
    )


@table_registry.mapped_as_dataclass
class Promocao:
    __tablename__ = 'promocoes'

    id: Mapped[int] = mapped_column(init=False, primary_key=True)

    porcentagem_desconto: Mapped[float]

    categoria_id: Mapped[int] = mapped_column(ForeignKey('categorias.id'))

    categoria: Mapped['Categoria'] = relationship(
        'Categoria',
        back_populates='promocao',
    )

    criado_em: Mapped[datetime] = mapped_column(
        init=False, server_default=func.now()
    )
    atualizado_em: Mapped[datetime] = mapped_column(
        init=False, onupdate=func.now(), default=func.now()
    )
