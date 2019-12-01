from flask_restful import Resource, marshal_with

from tenants.tenant_object import tenants_structure, list_tenants
from tenants.tenants_parser import parser_tenant


class GetTenants(Resource):
    method_decorators = [marshal_with(tenants_structure)]

    def get(self):
        if parser_tenant.parse_args().get('passportID') is None:
            return list_tenants
        else:
            return [ten for ten in list_tenants if parser_tenant.parse_args().get('passportID') == ten.passportID]

    def put(self, some_id):
        for ten in list_tenants:
            if ten.passportID == some_id:
                ten.room = parser_tenant.parse_args().get('room')
                return ten, 200
        else:
            return 404

    def delete(self):
        for ten in list_tenants:
            if parser_tenant.parse_args().get('passportID') == ten.passportID:
                list_tenants.remove(ten)
                return list_tenants, 200
            else:
                return 404
