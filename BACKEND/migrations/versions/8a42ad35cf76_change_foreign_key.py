"""change foreign key

Revision ID: 8a42ad35cf76
Revises: 4cdf176737b1
Create Date: 2021-05-09 13:16:49.402390

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a42ad35cf76'
down_revision = '4cdf176737b1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_countrydb_iso'), 'countrydb', ['iso'], unique=False)
    op.drop_constraint('peserta_ibfk_1', 'peserta', type_='foreignkey')
    op.create_foreign_key(None, 'peserta', 'countrydb', ['country_id'], ['iso'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'peserta', type_='foreignkey')
    op.create_foreign_key('peserta_ibfk_1', 'peserta', 'countrydb', ['country_id'], ['id'])
    op.drop_index(op.f('ix_countrydb_iso'), table_name='countrydb')
    # ### end Alembic commands ###
