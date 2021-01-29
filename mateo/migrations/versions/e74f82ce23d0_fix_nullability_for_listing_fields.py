"""Fix nullability for listing fields

Revision ID: e74f82ce23d0
Revises: 8c1a002a9bdc
Create Date: 2021-01-29 10:17:52.006980

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e74f82ce23d0'
down_revision = '8c1a002a9bdc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('listings', 'buyer_id',
               existing_type=postgresql.UUID(),
               nullable=False)
    op.alter_column('listings', 'seller_id',
               existing_type=postgresql.UUID(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('listings', 'seller_id',
               existing_type=postgresql.UUID(),
               nullable=False)
    op.alter_column('listings', 'buyer_id',
               existing_type=postgresql.UUID(),
               nullable=True)
    # ### end Alembic commands ###
