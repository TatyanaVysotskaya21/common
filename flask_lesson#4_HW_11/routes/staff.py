import json

from flask import Blueprint
from flask import request
from flask_restful import Resource, marshal_with

from db import db
from models.model import Staff, Rooms
from models.parser import staff_parser, staff_room_parser
from models.structures import staff_structure, room_structure

bp_staff = Blueprint("bp_staff", __name__)


class GetStaff(Resource):
    method_decorators = [marshal_with(staff_structure)]

    def get(self):
        if staff_parser.parse_args().get("passport_id") is not None:
            return Staff.query.get(staff_parser.parse_args().get("passport_id"))
        else:
            return Staff.query.all()

    def post(self):
        data = json.loads(request.data)
        room_id = data.pop("room_id")
        room = Rooms.query.get(room_id)
        data['rooms'] = [room]
        staff_obj = Staff(**data)
        db.session.add(staff_obj)
        db.session.commit()
        return "Successfully added the new Staff"

    def put(self, passport_id):
        body = json.loads(request.data)
        staff = Staff.query.get(passport_id)
        if body.get("room_id") in staff.rooms:
            staff.rooms.remove(body.get("rooms"))
        else:
            staff.rooms.append(body.get("rooms"))
        db.session.commit()
        return Staff.query.all()

    def delete(self, passport_id):
        staff = Staff.query.get(passport_id)
        db.session.delete(staff)
        db.session.commit()
        return Staff.query.all()


class StaffRoom(Resource):
    def post(self):
        data = json.loads(request.data)
        passport_id = data.get('passport_id')
        room_id = data.get('room_id')
        staff = Staff.query.filter_by(passport_id=passport_id).first()
        room = Rooms.query.filter_by(room_id=room_id).first()
        staff.rooms.append(room)
        db.session.commit()
        return f"Successfully added {room.room_id} to {staff.passport_id}"

    @marshal_with(room_structure)
    def get(self):
        args = staff_room_parser.parse_args().get("passport_id")
        staff = Staff.query.filter_by(passport_id=args).first()
        return staff.rooms
