"""FIXPKEYauto

Revision ID: 31d334438f7a
Revises: 1620d934155a
Create Date: 2021-05-10 14:52:08.166794

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '31d334438f7a'
down_revision = '1620d934155a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('peserta', sa.Column('id', sa.Integer(), autoincrement=True, nullable=False))
    op.drop_column('peserta', 'id_peserta')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('peserta', sa.Column('id_peserta', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.drop_column('peserta', 'id')
    # ### end Alembic commands ###
