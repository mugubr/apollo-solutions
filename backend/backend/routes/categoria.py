from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.database import get_session
from backend.models import Categoria
from backend.schemas.categoria import (
    CategoriaBaseSchema,
    CategoriaCreateSchema,
    CategoriaDB,
    CategoriaLista,
)

router = APIRouter(prefix='/categorias', tags=['Categorias'])


@router.get('/', response_model=CategoriaLista)
def read_categorias(
    limit: int = 10,
    offset: int = 0,
    session: Session = Depends(get_session),
):
    categorias = session.scalars(
        select(Categoria).limit(limit).offset(offset)
    ).all()
    return {'categorias': categorias}


@router.get('/{categoria_id}', response_model=CategoriaDB)
def read_categoria(
    categoria_id: int,
    session: Session = Depends(get_session),
):
    categoria = session.scalar(
        select(Categoria).where(Categoria.id == categoria_id)
    )
    if not categoria:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Categoria não encontrada'
        )
    return categoria


@router.post('/', response_model=CategoriaDB, status_code=HTTPStatus.CREATED)
def create_categoria(
    nova_categoria: CategoriaCreateSchema,
    session: Session = Depends(get_session),
):
    categoria_existente = session.scalar(
        select(Categoria).where(Categoria.nome == nova_categoria.nome)
    )
    if categoria_existente:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Categoria já cadastrada',
        )

    nova_categoria_db = Categoria(
        nome=nova_categoria.nome,
    )

    session.add(nova_categoria_db)
    session.commit()
    session.refresh(nova_categoria_db)

    return nova_categoria_db


@router.put('/{categoria_id}', response_model=CategoriaDB)
def update_categoria(
    categoria_id: int,
    categoria: CategoriaBaseSchema,
    session: Session = Depends(get_session),
):
    categoria_db = session.scalar(
        select(Categoria).where(Categoria.id == categoria_id)
    )
    if not categoria_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Categoria não encontrada'
        )

    categoria_db.nome = categoria.nome

    session.commit()
    session.refresh(categoria_db)

    return categoria_db


@router.delete('/{categoria_id}', response_model=dict)
def delete_categoria(
    categoria_id: int,
    session: Session = Depends(get_session),
):
    categoria_db = session.scalar(
        select(Categoria).where(Categoria.id == categoria_id)
    )
    if not categoria_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Categoria não encontrada'
        )
    session.delete(categoria_db)
    session.commit()
    return {'message': 'Categoria deletada'}
