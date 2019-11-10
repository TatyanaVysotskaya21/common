from flask_restful import Resource, marshal_with, fields

from tenants.tenant_object import Tenants
from tenants.tenants_parser import parser_tenant


list_tenants = [Tenants('Artur', 'AH768549', 29, 'M', {'sity': 'Dnipro',
                                                         'street': 'Shevchenko'}, 129),
                Tenants('Anna', 'AH769889', 36, 'F', {'sity': 'Lviv',
                                                        'street': 'Pugachova'}, 152),
                Tenants('Anton', 'AH078549', 19, 'M', {'sity': 'Dnipro',
                                                         'street': 'Savchenko'}, 198)]

adress_structure = {'sity': fields.String,
                    'street': fields.String}

tenants_structure = {'name': fields.String,
                     'passportID': fields.String,
                     'age': fields.Integer,
                     'sex': fields.String,
                     'adress': fields.Nested(adress_structure),
                     'room': fields.Integer}


class GetTenants(Resource):
    method_decorators = [marshal_with(tenants_structure)]

    def get(self):
        for ten in list_tenants:
            if parser_tenant.parse_args().get('passportID') == ten.passportID:
                return ten
        return list_tenants

    def put(self, id):
        for ten in list_tenants:
            if ten.passportID == id:
                ten.room = parser_tenant.parse_args().get('room')
                return ten, 200

    def delete(self):
        for ten in list_tenants:
            if parser_tenant.parse_args().get('passportID') == ten.passportID:
                list_tenants.remove(ten)
                return list_tenants, 200

