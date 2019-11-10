from flask import Flask

from config import run_config
from rooms.main_rooms import bp_rooms
from staff.main_staff import bp_staff
from tenants.main_tenants import bp_ten

app = Flask(__name__)
app.register_blueprint(bp_rooms)
app.register_blueprint(bp_staff)
app.register_blueprint(bp_ten)
app.config.from_object(run_config)


if __name__ == "__main__":
    app.run(debug=True)
