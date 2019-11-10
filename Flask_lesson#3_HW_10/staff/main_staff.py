from flask_restful import Api
from flask import Blueprint
from staff.staff_resourse import GetStaff

bp_staff = Blueprint("bp_staff", __name__)
api = Api(bp_staff)


api.add_resource(GetStaff, '/staff', '/staff/<string:id>')

