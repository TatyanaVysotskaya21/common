from flask_restful import reqparse


parser_room = reqparse.RequestParser(bundle_errors=True)
parser_room.add_argument('number', type=int)
parser_room.add_argument('status', type=str)

