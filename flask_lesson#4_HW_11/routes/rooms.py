import json

from flask import Blueprint
from flask import request
from flask_restful import Resource, marshal_with

from db import db
from models.model import Rooms
from models.parser import rooms_parser
from models.structures import room_structure

bp_rooms = Blueprint("bp_rooms", __name__)


class GetRooms(Resource):
    method_decorators = [marshal_with(room_structure)]

    def get(self):
        if rooms_parser.parse_args().get("room_id") is not None:
            return Rooms.query.get(rooms_parser.parse_args().get("room_id"))
        elif rooms_parser.parse_args().get("status") is not None:
            return Rooms.query.filter(Rooms.status.endswith(rooms_parser.parse_args().get("status"))).all()
        else:
            return Rooms.query.all()

    def post(self):
        data = json.loads(request.data)
        room_obj = Rooms(**data)
        db.session.add(room_obj)
        db.session.commit()
        return "Successfully added the new Room"

    def put(self, room_id):
        data = json.loads(request.data)
        room = Rooms.query.get(room_id)
        room.status = data.get("status")
        room.tenants_id = data.get("tenants_id")
        db.session.commit()
        return Rooms.query.all()

    def delete(self, room_id):
        room = Rooms.query.get(room_id)
        db.session.delete(room)
        db.session.commit()
        return Rooms.query.all()
