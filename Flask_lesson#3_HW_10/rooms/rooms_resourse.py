from flask_restful import Resource, marshal_with, fields

from rooms.room_object import Rooms
from rooms.rooms_parser import parser_room

list_rooms = [Rooms(235, "standart", "closed", 250),
              Rooms(826, "standart", "open", 250),
              Rooms(125, "lux", "open", 500)]

rooms_structure = {'number': fields.Integer,
                   'level': fields.String,
                   'status': fields.String,
                   'price': fields.Integer}


class GetRooms(Resource):
    method_decorators = [marshal_with(rooms_structure)]

    def get(self):
        get_rooms = {"number": [room for room in list_rooms if parser_room.parse_args().get('number') == room.number],
                     "status": [room for room in list_rooms if parser_room.parse_args().get('status') == room.status]}

        for key in parser_room.parse_args():
            return get_rooms.get(key)
        else:
            return [room for room in list_rooms]

    def post(self):
        list_rooms.append(Rooms(parser_room.parse_args().get('number'),
                                parser_room.parse_args().get('level'),
                                parser_room.parse_args().get('status'),
                                parser_room.parse_args().get('price')))
        return list_rooms, 200

    def put(self, id_room):
        for room in list_rooms:
            if room.number == id_room:
                room.status = parser_room.parse_args().get('status')
                return room, 200

    def delete(self):
        for room in list_rooms:
            if parser_room.parse_args().get('number') == room.number:
                list_rooms.remove(room)
                return list_rooms, 200
