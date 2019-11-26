from flask_restful import Resource, marshal_with

from staff.staff_object import staff_structure
from staff.staff_parser import parser_staff


class GetStaff(Resource):
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
            else:
                return 404

    def delete(self):
        for staff in self.list_staff:
            if parser_staff.parse_args().get("passportID") == staff.passportID:
                self.list_staff.remove(staff)
                return self.list_staff, 200
            else:
                return 404
