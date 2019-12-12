from datetime import timedelta

from flask import Flask
from flask_restful import Api

from config import run_config
from routes.create_db import CreateDB, create_db
from db import db
from routes.rooms import bp_rooms, GetRooms
from routes.staff import StaffRoom, GetStaff, bp_staff
from routes.tenants import bp_tenants, GetTenants


def create_app():
    app = Flask(__name__)
    api = Api(app)
    app.config.from_object(run_config())

    db.init_app(app)
    app.permanent_session_lifetime = timedelta(minutes=20)  # add session expire time

    app.register_blueprint(create_db)
    app.register_blueprint(bp_rooms)
    app.register_blueprint(bp_tenants)
    app.register_blueprint(bp_staff)

    api.add_resource(CreateDB, "/create_db")
    api.add_resource(GetRooms, "/room", "/room/<int:room_id>")
    api.add_resource(GetTenants, "/tenants", "/tenants/<int:passport_id>")
    api.add_resource(GetStaff, "/staff/<int:passport_id>")
    api.add_resource(StaffRoom, "/staffroom")

    return app
