from flask.views import MethodView
from flask_smorest import Blueprint
from flask_restful import Resource, reqparse
from models.booking import Booking
from db import db
from schemas import BookingSchema


blp = Blueprint("BookCall", "book_call", description="Operations for booking calls")


@blp.route("/book-call")
class BookCall(MethodView):
    @blp.arguments(BookingSchema)
    @blp.response(201, BookingSchema)
    def post(self, booking_data):
        """Book a call."""
        # Generate a unique Google Meet link
        meet_link = f"https://meet.google.com/session-{Booking.query.count() + 1}"
        booking_data["meet_link"] = meet_link

        # Create a new booking
        new_booking = Booking(**booking_data)
        db.session.add(new_booking)
        db.session.commit()

        return new_booking


@blp.route("/book-call/<int:booking_id>")
class BookingDetail(MethodView):
    @blp.response(200, BookingSchema)
    def get(self, booking_id):
        """Retrieve booking details by ID."""
        booking = Booking.query.get(booking_id)
        if not booking:
            return {"message": "Booking not found."}, 404

        return booking
    
    @blp.arguments(BookingSchema(partial=True))
    @blp.response(200, BookingSchema)
    def put(self, booking_data, booking_id):
        """Update booking details by ID."""
        booking = Booking.query.get(booking_id)
        if not booking:
            return {"message": "Booking not found."}, 404

        for key, value in booking_data.items():
            setattr(booking, key, value)

        db.session.commit()
        return booking

    @blp.response(200)
    def delete(self, booking_id):
        """Delete a booking by ID."""
        booking = Booking.query.get(booking_id)
        if not booking:
            return {"message": "Booking not found."}, 404

        db.session.delete(booking)
        db.session.commit()
        return {"message": "Booking deleted successfully."}