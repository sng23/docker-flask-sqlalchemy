import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()


class Cities(db.Model):
    __tablename__ = 'tblCitiesImport'
    fldName = db.Column(db.String(21), primary_key=True )