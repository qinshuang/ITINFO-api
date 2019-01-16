"""empty message

Revision ID: 1a6889cdcb27
Revises: dbb94ec672a5
Create Date: 2019-01-16 01:09:29.732137

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a6889cdcb27'
down_revision = 'dbb94ec672a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('servers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('server_name', sa.String(length=255), nullable=False),
    sa.Column('device_type', sa.String(length=50), nullable=False),
    sa.Column('os', sa.String(length=50), nullable=False),
    sa.Column('region', sa.String(length=50), nullable=False),
    sa.Column('cpu', sa.String(length=50), nullable=False),
    sa.Column('memory', sa.String(length=50), nullable=False),
    sa.Column('disk_type', sa.String(length=50), nullable=False),
    sa.Column('disk_volume', sa.String(length=50), nullable=False),
    sa.Column('comments', sa.String(length=255), nullable=True),
    sa.Column('normal_users', sa.String(length=255), nullable=True),
    sa.Column('sudo_users', sa.String(length=255), nullable=True),
    sa.Column('application_install', sa.String(length=255), nullable=True),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.Column('update_time', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('server_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('servers')
    # ### end Alembic commands ###