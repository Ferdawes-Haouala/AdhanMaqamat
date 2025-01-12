from flask.views import MethodView
from flask_smorest import Blueprint
from models.maqam_details import MaqamDetail
from models.maqam import Maqam
from db import db
from schemas import MaqamDetailSchema

blp = Blueprint("MaqamDetails", "maqam_details", description="Operations for Maqam Details")

@blp.route("/maqamat/<int:maqam_id>/details")
class MaqamDetails(MethodView):
    @blp.response(200, MaqamDetailSchema)
    def get(self, maqam_id):
        """Retrieve details for a specific Maqam."""
        details = MaqamDetail.query.filter_by(maqam_id=maqam_id).first()
        if not details:
            return {"message": "Details not found for this Maqam."}, 404
        return details

    @blp.arguments(MaqamDetailSchema)
    @blp.response(201, MaqamDetailSchema)
    def post(self, detail_data, maqam_id):
        """Add details to a Maqam."""
        if not Maqam.query.get(maqam_id):
            return {"message": "Maqam not found."}, 404

        detail_data["maqam_id"] = maqam_id
        new_detail = MaqamDetail(**detail_data)
        db.session.add(new_detail)
        db.session.commit()
        return new_detail

    @blp.arguments(MaqamDetailSchema(partial=True))
    @blp.response(200, MaqamDetailSchema)
    def put(self, detail_data, maqam_id):
        """Update details for a Maqam."""
        details = MaqamDetail.query.filter_by(maqam_id=maqam_id).first()
        if not details:
            return {"message": "Details not found for this Maqam."}, 404

        for key, value in detail_data.items():
            setattr(details, key, value)

        db.session.commit()
        return details
