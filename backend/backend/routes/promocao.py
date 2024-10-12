from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.database import get_session
from backend.models import Categoria, Promocao
from backend.schemas.promocao import (
    PromocaoBaseSchema,
    PromocaoCreateSchema,
    PromocaoDB,
    PromocaoLista,
)

router = APIRouter(prefix='/promocoes', tags=['Promoções'])


@router.get('/', response_model=PromocaoLista)
def read_promocoes(
    limit: int = 10,
    offset: int = 0,
    session: Session = Depends(get_session),
):
    promocoes = session.scalars(
        select(Promocao).limit(limit).offset(offset)
    ).all()
    return {'promocoes': promocoes}


@router.get('/{promocao_id}', response_model=PromocaoDB)
def read_promocao(
    promocao_id: int,
    session: Session = Depends(get_session),
):
    promocao = session.scalar(
        select(Promocao).where(Promocao.id == promocao_id)
    )
    if not promocao:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Promoção não encontrada'
        )
    return promocao


@router.post('/', response_model=PromocaoDB, status_code=HTTPStatus.CREATED)
def create_promocao(
    nova_promocao: PromocaoCreateSchema,
    session: Session = Depends(get_session),
):
    categoria_db = session.scalar(
        select(Categoria).where(Categoria.id == nova_promocao.categoria_id)
    )
    if not categoria_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Categoria não encontrada'
        )

    nova_promocao_db = Promocao(
        porcentagem_desconto=nova_promocao.porcentagem_desconto,
        categoria_id=nova_promocao.categoria_id,
        categoria=categoria_db,
    )

    session.add(nova_promocao_db)
    session.commit()
    session.refresh(nova_promocao_db)

    return nova_promocao_db


@router.put('/{promocao_id}', response_model=PromocaoDB)
def update_promocao(
    promocao_id: int,
    promocao: PromocaoBaseSchema,
    session: Session = Depends(get_session),
):
    promocao_db = session.scalar(
        select(Promocao).where(Promocao.id == promocao_id)
    )
    if not promocao_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Promoção não encontrada'
        )

    promocao_db.porcentagem_desconto = promocao.porcentagem_desconto
    promocao_db.categoria_id = promocao.categoria_id

    session.commit()
    session.refresh(promocao_db)

    return promocao_db


@router.delete('/{promocao_id}', response_model=dict)
def delete_promocao(
    promocao_id: int,
    session: Session = Depends(get_session),
):
    promocao_db = session.scalar(
        select(Promocao).where(Promocao.id == promocao_id)
    )
    if not promocao_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Promoção não encontrada'
        )
    session.delete(promocao_db)
    session.commit()
    return {'message': 'Promoção deletada'}
