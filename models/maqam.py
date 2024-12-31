from db import db
from marshmallow import Schema, fields

class Maqam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    links = db.Column(db.JSON)  # List of URLs
