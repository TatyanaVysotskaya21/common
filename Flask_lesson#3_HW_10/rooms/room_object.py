from flask_restful import fields


class Rooms:
    def __init__(self, number, level, status, price):
        self.number = number
        self.level = level
        self.status = status
        self.price = price


list_rooms = [Rooms(235, "standart", "closed", 250),
              Rooms(826, "standart", "open", 250),
              Rooms(125, "lux", "open", 500)]

rooms_structure = {'number': fields.Integer,
                   'level': fields.String,
                   'status': fields.String,
                   'price': fields.Integer}
