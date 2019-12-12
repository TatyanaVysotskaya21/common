from flask_restful import reqparse

tenants_parser = reqparse.RequestParser()
tenants_parser.add_argument('passport_id', type=int)

rooms_parser = reqparse.RequestParser()
rooms_parser.add_argument('room_id', type=int)
rooms_parser.add_argument('status', type=str)

staff_parser = reqparse.RequestParser()
staff_parser.add_argument('passport_id', required=True)

staff_room_parser = reqparse.RequestParser()
staff_room_parser.add_argument('passport_id', required=True)
