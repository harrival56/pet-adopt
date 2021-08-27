from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy.sql.expression import false

db = SQLAlchemy()
def connect_db(app):
    db.app = app
    db.init_app(app)



class Pet(db.Model):
    """Pets model """
    __tablename__ = "pets"


    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    note = db.Column(db.Text)
    available = db.Column(db.Boolean, default=True)

    def __repr__(self):
        p = self
        return (f"pet=> ID={p.id}, name={p.name}, species={p.name}, photo_url={p.photo_url}, age={p.age}, note={p.note}, available={p.available}")
        