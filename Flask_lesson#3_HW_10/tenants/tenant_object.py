from flask_restful import fields


class Tenants:
    def __init__(self, name, passportID, age, sex, adress, room):
        self.name = name
        self.passportID = passportID
        self.age = age
        self.sex = sex
        self.adress = adress
        self.room = room


list_tenants = [Tenants('Artur', 'AH768549', 29, 'M', {'sity': 'Dnipro', 'street': 'Shevchenko'}, 129),
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
