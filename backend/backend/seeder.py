from contextlib import contextmanager

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session, sessionmaker

from backend.models import Categoria, Produto, Promocao
from backend.schemas.produto import ProdutoCreateSchema

DATABASE_URL = (
    'postgresql+psycopg://app_user:app_password@apollo_database:5432/app_db'
)
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@contextmanager
def get_session():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


def create_categoria(session: Session, nome: str):
    categoria_existente = session.scalar(
        select(Categoria).where(Categoria.nome == nome)
    )
    if not categoria_existente:
        nova_categoria = Categoria(nome=nome)
        session.add(nova_categoria)
        session.commit()
        session.refresh(nova_categoria)
        return nova_categoria
    return categoria_existente


def create_produto(session: Session, produto: ProdutoCreateSchema):
    produto_existente = session.scalar(
        select(Produto).where(Produto.nome == produto.nome)
    )
    if not produto_existente:
        categoria = session.scalar(
            select(Categoria).where(Categoria.id == produto.categoria_id)
        )
        novo_produto = Produto(
            nome=produto.nome,
            descricao=produto.descricao,
            cor=produto.cor,
            preco=produto.preco,
            categoria_id=produto.categoria_id,
            categoria=categoria,
        )
        session.add(novo_produto)
        session.commit()
        session.refresh(novo_produto)
        return novo_produto
    return produto_existente


def create_promocao(
    session: Session, porcentagem_desconto: float, categoria_id: int
):
    promocao_existente = session.scalar(
        select(Promocao).where(Promocao.categoria_id == categoria_id)
    )
    if not promocao_existente:
        categoria = session.scalar(
            select(Categoria).where(Categoria.id == categoria_id)
        )
        nova_promocao = Promocao(
            porcentagem_desconto=porcentagem_desconto,
            categoria_id=categoria_id,
            categoria=categoria,
        )
        session.add(nova_promocao)
        session.commit()
        session.refresh(nova_promocao)
        return nova_promocao
    return promocao_existente


def main():
    with get_session() as session:
        categoria1 = create_categoria(session, 'Smartphones')
        categoria2 = create_categoria(session, 'Móveis')
        categoria3 = create_categoria(session, 'Eletrônicos')
        categoria4 = create_categoria(session, 'Eletroportáteis')
        categoria5 = create_categoria(session, 'Geladeiras')

        create_produto(
            session,
            ProdutoCreateSchema(
                nome='iPhone',
                descricao='iPhone 15 Pro Max',
                cor='Titânio Natural',
                preco=10999,
                categoria_id=categoria1.id,
            ),
        )
        create_produto(
            session,
            ProdutoCreateSchema(
                nome='Guarda roupas',
                descricao='4 portas, 6 gavetas',
                cor='Verniz',
                preco=799.89,
                categoria_id=categoria2.id,
            ),
        )
        create_produto(
            session,
            ProdutoCreateSchema(
                nome='Home theater',
                descricao='Bluetooth wireless soundbar',
                cor='Prata',
                preco=1299,
                categoria_id=categoria3.id,
            ),
        )
        create_produto(
            session,
            ProdutoCreateSchema(
                nome='Torradeira',
                descricao='Espaço para 2 fatias de pão',
                cor='Preto',
                preco=149.9,
                categoria_id=categoria4.id,
            ),
        )
        create_produto(
            session,
            ProdutoCreateSchema(
                nome='Geladeira',
                descricao='2 portas e com freezer',
                cor='Branco',
                preco=4789.89,
                categoria_id=categoria5.id,
            ),
        )

        create_promocao(session, 2.55, categoria1.id)
        create_promocao(session, 3, categoria2.id)
        create_promocao(session, 4.3, categoria3.id)
        create_promocao(session, 5, categoria4.id)
        create_promocao(session, 7.5, categoria5.id)


if __name__ == '__main__':
    main()
