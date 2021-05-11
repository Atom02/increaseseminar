from project import mariadb

class Peserta(mariadb.Model):
    id = mariadb.Column('id', mariadb.Integer, primary_key=True, autoincrement=True)
    email = mariadb.Column('email', mariadb.String(255), nullable=False)
    name = mariadb.Column('name',mariadb.String(255), nullable=False)
    affiliation = mariadb.Column('affiliation', mariadb.String(500), nullable=False)
    uniqueURL = mariadb.Column('url_key', mariadb.String(500), unique=True, nullable=False)
    country_id = mariadb.Column('country_id', mariadb.Integer, mariadb.ForeignKey('countrydb.id', ondelete='SET NULL'))