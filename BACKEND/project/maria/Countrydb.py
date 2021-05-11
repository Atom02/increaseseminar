from project import mariadb

class Countrydb(mariadb.Model):
    id = mariadb.Column('id', mariadb.Integer, primary_key=True, autoincrement=True)
    iso = mariadb.Column('iso',mariadb.String(2), nullable=False, unique=True, index=True)
    name = mariadb.Column('name', mariadb.String(80), nullable=False)
    nicename = mariadb.Column('nicename', mariadb.String(80), nullable=False)
    iso3 = mariadb.Column('iso3', mariadb.String(3))
    numcode = mariadb.Column('numcode', mariadb.Integer)
    phoncode = mariadb.Column('phonecode', mariadb.Integer)
    pesertaRealtion = mariadb.relationship('Peserta', backref='nationality', lazy=True)