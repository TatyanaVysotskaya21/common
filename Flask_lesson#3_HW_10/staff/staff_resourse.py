from flask_restful import Resource, marshal_with, fields

from staff.staff_object import Staff
from staff.staff_parser import parser_staff


class GetStaff(Resource):
    staff_structure = {'name': fields.String,
                       'passportID': fields.String,
                       'position': fields.String,
                       'salary': fields.Integer}

    def __init__(self):
        self.list_staff = [Staff("Anna", "AH586898", "chambermaid", 5550),
                           Staff("Alex", "AH582564", "administrator", 7000),
                           Staff("David", "AH369647", "receptionist", 6000)]

    method_decorators = [marshal_with(staff_structure)]

    def get(self):
        if parser_staff.parse_args().get('passportID') is None:
            return self.list_staff
        else:
            return [staff for staff in self.list_staff if
                    parser_staff.parse_args().get('passportID') == staff.passportID]

    def put(self, some_id):
        for staff in self.list_staff:
            if staff.passportID == some_id:
                staff.salary = parser_staff.parse_args().get('salary')
                return staff, 200

    def delete(self):
        for staff in self.list_staff:
            if parser_staff.parse_args().get("passportID") == staff.passportID:
                self.list_staff.remove(staff)
                return self.list_staff, 200
