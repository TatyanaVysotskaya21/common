from flask_restful import fields


class Staff:
    def __init__(self, name, passportID, position, salary):
        self.name = name
        self.passportID = passportID
        self.position = position
        self.salary = salary


staff_structure = {'name': fields.String,
                   'passportID': fields.String,
                   'position': fields.String,
                   'salary': fields.Integer}

list_staff = [Staff("Anna", "AH586898", "chambermaid", 5550),
              Staff("Alex", "AH582564", "administrator", 7000),
              Staff("David", "AH369647", "receptionist", 6000)]
