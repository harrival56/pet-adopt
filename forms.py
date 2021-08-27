from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField


class AddPet(FlaskForm):
    """Form for adding pet"""
    name = StringField("Name")
    species = StringField("Species")
    photo_url =StringField("Photo")
    age =IntegerField("Age")
    note = StringField("Note")
    available = BooleanField("Available")