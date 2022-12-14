"""empty message

Revision ID: 67a36642b525
Revises: 307bb134aefe
Create Date: 2022-09-07 16:47:53.718193

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67a36642b525'
down_revision = '307bb134aefe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
