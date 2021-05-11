from project import db
class Peserta(db.Document):
    email = db.EmailField(required=True, Unique=True)
    name = db.StringField(required=True)
    affiliation = db.StringField(required=True)
    interest = db.StringField()