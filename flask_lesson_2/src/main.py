from datetime import timedelta

from flask import Flask, render_template, session
from src.product.blueprint_product import product
from src.supermarket.blueprint_supermarkets import markets


app = Flask(__name__, template_folder='templates')

app.register_blueprint(markets)
app.register_blueprint(product)


app.config['SECRET_KEY'] = 'a really really really really long secret key'
app.config['SESSION_TYPE'] = 'filesystem'
app.permanent_session_lifetime = timedelta(seconds=10)


@app.route("/")
def get_home():
    return render_template("base.html")


@app.errorhandler(404)
def page_error(error):
    return render_template('error_404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)

