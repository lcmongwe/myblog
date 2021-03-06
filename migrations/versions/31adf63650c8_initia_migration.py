"""initia Migration

Revision ID: 31adf63650c8
Revises: c4d7b45e70bf
Create Date: 2022-05-19 14:32:50.384827

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31adf63650c8'
down_revision = 'c4d7b45e70bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('likes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('likes',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='likes_pkey')
    )
    # ### end Alembic commands ###
