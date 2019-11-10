from flask_restful import Resource, marshal_with, fields

from staff.staff_object import Staff
from staff.staff_parser import parser_staff


list_staff = [Staff("Anna", "AH586898", "chambermaid", 5550),
              Staff("Alex", "AH582564", "administrator", 7000),
              Staff("David", "AH369647", "receptionist", 6000)]

staff_structure = {'name': fields.String,
                   'passportID': fields.String,
                   'position': fields.String,
                   'salary': fields.Integer}


class GetStaff(Resource):
    method_decorators = [marshal_with(staff_structure)]

    def get(self):
        for staff in list_staff:
            if parser_staff.parse_args().get("passportID") == staff.passportID:
                return staff
        return list_staff

    def delete(self):
        for staff in list_staff:
            if parser_staff.parse_args().get("passportID") == staff.passportID:
                list_staff.remove(staff)
                return list_staff, 200

