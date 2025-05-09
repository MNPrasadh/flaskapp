"""Add fairness column to

Revision ID: 885d16d50bb4
Revises: 9d9357b579cc
Create Date: 2025-04-27 18:01:26.816760

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '885d16d50bb4'
down_revision = '9d9357b579cc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('last_updated_time', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('last_updated_time')

    # ### end Alembic commands ###
