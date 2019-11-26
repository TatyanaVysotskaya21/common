from flask_restful import Resource, marshal_with

from rooms.room_object import Rooms, rooms_structure, list_rooms
from rooms.rooms_parser import parser_room


class GetRooms(Resource):
    method_decorators = [marshal_with(rooms_structure)]

    def get(self):
        get_rooms = {
            "number": [room for room in list_rooms if parser_room.parse_args().get('number') == room.number],
            "status": [room for room in list_rooms if parser_room.parse_args().get('status') == room.status]}

        for key, value in parser_room.parse_args().items():
            if value is not None:
                return get_rooms.get(key)
        else:
            return list_rooms

    def post(self):
        for obj_room in list_rooms:
            if obj_room.number == parser_room.parse_args().get('number'):
                return "such number already exists"
        if parser_room.parse_args().get('number') <= 0:
            return "number cannot have a negative value"
        list_rooms.append(Rooms(**parser_room.parse_args()))
        return "ok"

    def put(self, id_room):
        for room in list_rooms:
            if room.number == id_room:
                room.status = parser_room.parse_args().get('status')
                return "ok", 200
            else:
                return 404

    def delete(self):
        for room in list_rooms:
            if parser_room.parse_args().get('number') == room.number:
                list_rooms.remove(room)
                return "ok", 200
            else:
                return 404
