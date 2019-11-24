from db import db


class Tenants(db.Model):
    passport_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    sex = db.Column(db.String)
    address = db.Column(db.String)
    city = db.Column(db.String)
    rooms = db.relationship('Rooms', backref='tenants')


staff_room = db.Table(
    'staff_room',
    db.Column('passport_id', db.Integer, db.ForeignKey('Staff.passport_id')),
    db.Column('room_id', db.Integer, db.ForeignKey('Rooms.room_id')))


class Rooms(db.Model):
    room_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    level = db.Column(db.String)
    status = db.Column(db.String)
    price = db.Column(db.Integer)
    tenants_id = db.Column(db.Integer, db.ForeignKey('tenants.passport_id'))


class Staff(db.Model):
    passport_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    position = db.Column(db.String)
    salary = db.Column(db.String)
    rooms = db.relationship('Rooms', secondary=staff_room, backref=db.backref('staff'))
