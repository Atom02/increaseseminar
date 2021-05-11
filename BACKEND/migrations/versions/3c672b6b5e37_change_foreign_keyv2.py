"""change foreign keyv2

Revision ID: 3c672b6b5e37
Revises: 52829bd20042
Create Date: 2021-05-09 13:57:58.759082

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3c672b6b5e37'
down_revision = '52829bd20042'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'peserta', 'countrydb', ['country_id'], ['id'], ondelete='SET NULL')
    op.drop_column('peserta', 'country')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('peserta', sa.Column('country', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'peserta', type_='foreignkey')
    # ### end Alembic commands ###
