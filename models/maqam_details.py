from db import db
from marshmallow import Schema, fields

class MaqamDetail(db.Model):
    __tablename__ = "maqam_details"

    id = db.Column(db.Integer, primary_key=True)
    maqam_id = db.Column(db.Integer, db.ForeignKey("maqam.id"), nullable=False)
    rekaz = db.Column(db.String(80), nullable=True)  # Tonal center
    awarid = db.Column(db.String(200), nullable=True)  # Variations
    oqoud = db.Column(db.String(200), nullable=True)  # Melodic sequences
    maqam = db.relationship("Maqam", backref="details")
