import json

from flask import Blueprint
from flask import request
from flask_restful import Resource, marshal_with

from db import db
from models.model import Tenants, Rooms
from models.parser import tenants_parser
from models.structures import tenants_structure

bp_tenants = Blueprint("bp_tenants", __name__)


class GetTenants(Resource):
    method_decorators = [marshal_with(tenants_structure)]

    def get(self):
        if tenants_parser.parse_args().get("passport_id") is not None:
            return Tenants.query.get(tenants_parser.parse_args().get("passport_id"))
        else:
            return Tenants.query.all()

    def post(self):
        data = json.loads(request.data)
        room_id = data.pop("room_id")
        room = Rooms.query.get(room_id)
        data['rooms'] = [room]
        tenant = Tenants(**data)
        db.session.add(tenant)
        db.session.commit()
        return "Successfully added the new Tenant"

    def put(self, passport_id):
        data = json.loads(request.data)
        tenants = Tenants.query.get(passport_id)
        if data.get("room_id") in tenants.rooms:
            tenants.rooms.remove(data.get("rooms"))
        else:
            tenants.rooms.append(data.get("rooms"))
        db.session.commit()
        return Tenants.query.all()

    def delete(self, passport_id):
        tenants = Tenants.query.get(passport_id)
        db.session.delete(tenants)
        db.session.commit()
        return Tenants.query.all()
