from flask_restful import reqparse

parser_tenant = reqparse.RequestParser(bundle_errors=True)
parser_tenant.add_argument('passportID', type=str)
parser_tenant.add_argument('room', type=int)
