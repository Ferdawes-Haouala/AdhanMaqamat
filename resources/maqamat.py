from flask_restful import Resource, reqparse
from models.maqam import Maqam
from schemas import MaqamSchema
from db import db

maqam_schema = MaqamSchema()
maqam_list_schema = MaqamSchema(many=True)

class MaqamatList(Resource):
    def get(self):
        maqamat = Maqam.query.all()
        return maqam_list_schema.dump(maqamat), 200

class MaqamUpload(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str, required=True, help="Name is required.")
        parser.add_argument("description", type=str, required=True, help="Description is required.")
        parser.add_argument("links", type=list, location="json", required=True, help="Links are required.")
        data = parser.parse_args()

        new_maqam = Maqam(name=data["name"], description=data["description"], links=data["links"])
        db.session.add(new_maqam)
        db.session.commit()

        return {"message": "Maqam uploaded successfully.", "maqam": maqam_schema.dump(new_maqam)}, 201

class MaqamDetail(Resource):
    def get(self, maqam_id):
        maqam = Maqam.query.get(maqam_id)
        if not maqam:
            return {"message": "Maqam not found."}, 404
        return maqam_schema.dump(maqam), 200

    def put(self, maqam_id):
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str, required=False)
        parser.add_argument("description", type=str, required=False)
        parser.add_argument("links", type=list, location="json", required=False)
        data = parser.parse_args()

        maqam = Maqam.query.get(maqam_id)
        if not maqam:
            return {"message": "Maqam not found."}, 404

        if data["name"]:
            maqam.name = data["name"]
        if data["description"]:
            maqam.description = data["description"]
        if data["links"]:
            maqam.links = data["links"]

        db.session.commit()
        return {"message": "Maqam updated successfully.", "maqam": maqam_schema.dump(maqam)}, 200

    def delete(self, maqam_id):
        maqam = Maqam.query.get(maqam_id)
        if not maqam:
            return {"message": "Maqam not found."}, 404
        db.session.delete(maqam)
        db.session.commit()
        return {"message": "Maqam deleted successfully."}, 200
