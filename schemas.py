from marshmallow import Schema, fields

# Maqam Schema
class MaqamSchema(Schema):
    id = fields.Int(dump_only=True)  # Read-only field
    name = fields.Str(required=True)  # Required input
    description = fields.Str(required=True)
    links = fields.List(fields.Str(), required=True)

# User Schema
class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=False)
    email = fields.Email(required=True)
    password = fields.Str(required=True, load_only=True)
    

    
# Booking Schema 
class BookingSchema(Schema):
    id = fields.Int(dump_only=True)  # Read-only field
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    topic = fields.Str(required=True)
    datetime = fields.Str(required=True)
    meet_link = fields.Str(dump_only=True)  # Generated dynamically
    
    
    # Marshmallow schema for MaqamDetail
class MaqamDetailSchema(Schema):
    id = fields.Int(dump_only=True)  # Read-only field
    maqam_id = fields.Int(required=True)  # Foreign key to Maqam
    rekaz = fields.Str(required=False)  # Optional
    awarid = fields.Str(required=False)  # Optional
    oqoud = fields.Str(required=False)  # Optional

