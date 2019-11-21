from flask import Blueprint
from flask_restful import Api

from tenants.tenants_resourse import GetTenants

bp_ten = Blueprint("bp_ten", __name__)
api = Api(bp_ten)

api.add_resource(GetTenants, '/tenants', '/tenants/<string:id>')
