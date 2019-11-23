from flask_restful import Resource, marshal_with, fields

from tenants.tenant_object import Tenants
from tenants.tenants_parser import parser_tenant


class GetTenants(Resource):
    def __init__(self):
        self.list_tenants = [Tenants('Artur', 'AH768549', 29, 'M', {'sity': 'Dnipro', 'street': 'Shevchenko'}, 129),
                             Tenants('Anna', 'AH769889', 36, 'F', {'sity': 'Lviv', 'street': 'Pugachova'}, 152),
                             Tenants('Anton', 'AH078549', 19, 'M', {'sity': 'Dnipro', 'street': 'Savchenko'}, 198)]

    address_structure = {'sity': fields.String,
                         'street': fields.String}

    tenants_structure = {'name': fields.String,
                         'passportID': fields.String,
                         'age': fields.Integer,
                         'sex': fields.String,
                         'address': fields.Nested(address_structure),
                         'room': fields.Integer}
    method_decorators = [marshal_with(tenants_structure)]

    def get(self):
        if parser_tenant.parse_args().get('passportID') is None:
            return self.list_tenants
        else:
            return [ten for ten in self.list_tenants if parser_tenant.parse_args().get('passportID') == ten.passportID]

    def put(self, some_id):
        for ten in self.list_tenants:
            if ten.passportID == some_id:
                ten.room = parser_tenant.parse_args().get('room')
                return ten, 200
            else:
                return 404

    def delete(self):
        for ten in self.list_tenants:
            if parser_tenant.parse_args().get('passportID') == ten.passportID:
                self.list_tenants.remove(ten)
                return self.list_tenants, 200
            else:
                return 404
