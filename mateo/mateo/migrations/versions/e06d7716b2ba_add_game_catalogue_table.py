"""Add game catalogue table

Revision ID: e06d7716b2ba
Revises: 9262e56c4ad1
Create Date: 2021-01-28 16:50:23.888084

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e06d7716b2ba'
down_revision = '9262e56c4ad1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('games',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('title', sa.String(length=256), nullable=False),
    sa.Column('platform', sa.String(length=64), nullable=False),
    sa.Column('image', sa.String(length=1024), nullable=True),
    sa.Column('listing_count', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('games')
    # ### end Alembic commands ###
