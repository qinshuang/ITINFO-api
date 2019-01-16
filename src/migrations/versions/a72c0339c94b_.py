"""empty message

Revision ID: a72c0339c94b
Revises: 0643f78085b3
Create Date: 2019-01-16 02:17:23.826630

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a72c0339c94b'
down_revision = '0643f78085b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('servers', sa.Column('status', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('servers', 'status')
    # ### end Alembic commands ###