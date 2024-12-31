from db import db

class Upload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    maqam_id = db.Column(db.Integer, db.ForeignKey('maqam.id'))
    file_url = db.Column(db.String(200), nullable=False)
    is_approved = db.Column(db.Boolean, default=False)
