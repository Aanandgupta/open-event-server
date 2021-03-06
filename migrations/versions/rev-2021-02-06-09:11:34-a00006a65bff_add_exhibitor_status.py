"""Add exhibitor.status

Revision ID: a00006a65bff
Revises: 16d8d69a64e4
Create Date: 2021-02-06 09:11:34.071168

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = 'a00006a65bff'
down_revision = '16d8d69a64e4'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('exhibitors', sa.Column('status', sa.String(), server_default='pending', nullable=False))
    op.execute("update exhibitors set status = 'accepted'")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('exhibitors', 'status')
    # ### end Alembic commands ###
