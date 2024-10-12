from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import asc, desc, select
from sqlalchemy.orm import Session

from backend.database import get_session
from backend.models import Categoria, Produto
from backend.schemas.produto import (
    ProdutoBaseSchema,
    ProdutoCreateSchema,
    ProdutoDB,
    ProdutoLista,
    ProdutoQueryParams,
)

router = APIRouter(prefix='/produtos', tags=['Produtos'])


@router.get('/', response_model=ProdutoLista)
def read_produtos(
    query_params: ProdutoQueryParams = Depends(),
    session: Session = Depends(get_session),
):
    query = select(Produto)

    if query_params.nome:
        query = query.where(Produto.nome.ilike(f'%{query_params.nome}%'))
    if query_params.categoria_id:
        query = query.where(Produto.categoria_id == query_params.categoria_id)

    if query_params.order_direction == 'desc':
        query = query.order_by(desc(query_params.order_by))
    else:
        query = query.order_by(asc(query_params.order_by))

    produtos = session.scalars(
        query.limit(query_params.limit).offset(query_params.offset)
    ).all()

    return {'produtos': produtos}


@router.get('/{produto_id}', response_model=ProdutoDB)
def read_produto(
    produto_id: int,
    session: Session = Depends(get_session),
):
    produto = session.scalar(select(Produto).where(Produto.id == produto_id))
    if not produto:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Produto não encontrado'
        )

    return produto


@router.post('/', response_model=ProdutoDB, status_code=HTTPStatus.CREATED)
def create_produto(
    novo_produto: ProdutoCreateSchema,
    session: Session = Depends(get_session),
):
    produto_existente = session.scalar(
        select(Produto).where(Produto.nome == novo_produto.nome)
    )
    if produto_existente:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Produto já cadastrado',
        )

    categoria_db = session.scalar(
        select(Categoria).where(Categoria.id == novo_produto.categoria_id)
    )
    if not categoria_db:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Categoria não encontrada',
        )

    novo_produto_db = Produto(
        nome=novo_produto.nome,
        descricao=novo_produto.descricao,
        cor=novo_produto.cor,
        preco=novo_produto.preco,
        categoria_id=novo_produto.categoria_id,
        categoria=categoria_db,
    )

    session.add(novo_produto_db)
    session.commit()
    session.refresh(novo_produto_db)

    return novo_produto_db


@router.put('/{produto_id}', response_model=ProdutoDB)
def update_produto(
    produto_id: int,
    produto_atualizado: ProdutoBaseSchema,
    session: Session = Depends(get_session),
):
    produto_db = session.scalar(
        select(Produto).where(Produto.id == produto_id)
    )
    if not produto_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Produto não encontrado'
        )

    categoria = session.scalar(
        select(Categoria).where(
            Categoria.id == produto_atualizado.categoria_id
        )
    )
    if not categoria:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Categoria não encontrada',
        )

    produto_db.nome = produto_atualizado.nome
    produto_db.descricao = produto_atualizado.descricao
    produto_db.cor = produto_atualizado.cor
    produto_db.preco = produto_atualizado.preco
    produto_db.categoria_id = produto_atualizado.categoria_id

    session.commit()
    session.refresh(produto_db)

    return produto_db


@router.delete('/{produto_id}', response_model=dict)
def delete_produto(
    produto_id: int,
    session: Session = Depends(get_session),
):
    produto_db = session.scalar(
        select(Produto).where(Produto.id == produto_id)
    )
    if not produto_db:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='Produto não encontrado'
        )

    session.delete(produto_db)
    session.commit()

    return {'message': 'Produto deletado'}
