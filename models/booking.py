from db import db

class Booking(db.Model):
    __tablename__ = "bookings"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    topic = db.Column(db.String(120), nullable=False)
    datetime = db.Column(db.String(120), nullable=False)
    meet_link = db.Column(db.String(200), nullable=False)
