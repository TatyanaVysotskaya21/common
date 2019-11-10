from flask_restful import reqparse

parser_staff = reqparse.RequestParser(bundle_errors=True)
parser_staff.add_argument('passportID', type=str)
parser_staff.add_argument('salary', type=int)

