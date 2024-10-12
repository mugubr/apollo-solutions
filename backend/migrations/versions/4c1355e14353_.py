"""empty message

Revision ID: 4c1355e14353
Revises: 
Create Date: 2024-10-11 17:36:30.902606

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4c1355e14353'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('produtos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=False),
    sa.Column('descricao', sa.String(), nullable=False),
    sa.Column('cor', sa.String(), nullable=False),
    sa.Column('categoria', sa.Integer(), nullable=False),
    sa.Column('preco', sa.Float(), nullable=False),
    sa.Column('preco_promocional', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nome')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('produtos')
    # ### end Alembic commands ###
