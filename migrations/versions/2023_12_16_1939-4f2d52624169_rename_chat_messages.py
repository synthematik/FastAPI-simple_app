"""Rename: Chat --> Messages

Revision ID: 4f2d52624169
Revises: 72718dcdd66c
Create Date: 2023-12-16 19:39:59.808663

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4f2d52624169'
down_revision: Union[str, None] = '72718dcdd66c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('message', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('chat')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chat',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('message', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='chat_pkey')
    )
    op.drop_table('messages')
    # ### end Alembic commands ###
