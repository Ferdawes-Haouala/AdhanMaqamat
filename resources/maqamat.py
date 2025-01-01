from flask.views import MethodView
from flask_smorest import Blueprint
from flask import request
from flask_restful import Resource, reqparse
from models.maqam import Maqam
from schemas import MaqamSchema
from db import db

blp = Blueprint("Maqamat", "maqamat", description="Operations on Maqamat")

@blp.route("/maqamat")
class MaqamatList(MethodView):
    @blp.response(200, MaqamSchema(many=True))
    def get(self):
        """Get all Maqamat."""
        maqamat = Maqam.query.all()
        return maqamat

@blp.route("/maqamat/upload")
class MaqamUpload(MethodView):
    @blp.arguments(MaqamSchema)
    @blp.response(201, MaqamSchema)
    def post(self, maqam_data):
        """Upload a new Maqam."""
        new_maqam = Maqam(**maqam_data)
        db.session.add(new_maqam)
        db.session.commit()
        return new_maqam

@blp.route("/maqamat/<int:maqam_id>")
class MaqamDetail(MethodView):
    @blp.response(200, MaqamSchema)
    def get(self, maqam_id):
        """Get a Maqam by ID."""
        maqam = Maqam.query.get(maqam_id)
        if not maqam:
            return {"message": "Maqam not found."}, 404
        return maqam

    @blp.arguments(MaqamSchema(partial=True))
    @blp.response(200, MaqamSchema)
    def put(self, maqam_data, maqam_id):
        """Update a Maqam by ID."""
        maqam = Maqam.query.get(maqam_id)
        if not maqam:
            return {"message": "Maqam not found."}, 404

        for key, value in maqam_data.items():
            setattr(maqam, key, value)

        db.session.commit()
        return maqam

    @blp.response(200)
    def delete(self, maqam_id):
        """Delete a Maqam by ID."""
        maqam = Maqam.query.get(maqam_id)
        if not maqam:
            return {"message": "Maqam not found."}, 404

        db.session.delete(maqam)
        db.session.commit()
        return {"message": "Maqam deleted successfully."}