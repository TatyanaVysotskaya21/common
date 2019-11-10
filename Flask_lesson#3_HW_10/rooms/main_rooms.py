from flask_restful import Api
from flask import Blueprint
from rooms.rooms_resourse import GetRooms

bp_rooms = Blueprint("bp_rooms", __name__)
api = Api(bp_rooms)


api.add_resource(GetRooms, '/rooms', '/rooms/<int:id_room>')

