from flask_restful import reqparse

parser_tenant = reqparse.RequestParser(bundle_errors=True)
parser_tenant.add_argument('passportID', type=str)
parser_tenant.add_argument('room', type=int)
parser_tenant.add_argument('name', type=str)
parser_tenant.add_argument('age', type=int)
parser_tenant.add_argument('sex', type=str)
parser_tenant.add_argument('address', type=str)
