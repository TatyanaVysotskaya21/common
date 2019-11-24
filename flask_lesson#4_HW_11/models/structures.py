from flask_restful import fields

room_structure = {
    "room_id": fields.Integer,
    "level": fields.String,
    "status": fields.String,
    "price": fields.Integer,
    "tenants_id": fields.Integer
}

tenants_structure = {
    "passport_id": fields.Integer,
    "name": fields.String,
    "age": fields.String,
    "sex": fields.String,
    "city": fields.String,
    "address": fields.String,
    "rooms": fields.List
}

staff_structure = {
    'passport_id': fields.Integer,
    'name': fields.String,
    'position': fields.String,
    'salary': fields.Integer,
    'rooms': fields.List
}
