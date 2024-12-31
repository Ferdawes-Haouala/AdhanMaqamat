from flask_restful import Resource, reqparse
from models.booking import Booking
from db import db
from schemas import BookingSchema

booking_schema = BookingSchema()


class BookCall(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str, required=True, help="Name is required.")
        parser.add_argument("email", type=str, required=True, help="Email is required.")
        parser.add_argument("topic", type=str, required=True, help="Topic is required.")
        parser.add_argument("datetime", type=str, required=True, help="Date and time are required.")
        data = parser.parse_args()

        meet_link = f"https://meet.google.com/session-{Booking.query.count() + 1}"

        new_booking = Booking(
            name=data["name"],
            email=data["email"],
            topic=data["topic"],
            datetime=data["datetime"],
            meet_link=meet_link,
        )
        db.session.add(new_booking)
        db.session.commit()

        return {
            "message": "Call booked successfully.",
            "booking": {
                "id": new_booking.id,
                "name": new_booking.name,
                "email": new_booking.email,
                "topic": new_booking.topic,
                "datetime": new_booking.datetime,
                "meet_link": new_booking.meet_link,
            },
        }, 201


class BookingDetail(Resource):
    def get(self, booking_id):
        booking = Booking.query.get(booking_id)
        if not booking:
            return {"message": "Booking not found."}, 404

        return {
            "id": booking.id,
            "name": booking.name,
            "email": booking.email,
            "topic": booking.topic,
            "datetime": booking.datetime,
            "meet_link": booking.meet_link,
        }, 200
