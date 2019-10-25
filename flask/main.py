from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def get_home():
    return render_template('home.html')


@app.route("/vegetables")
def get_vegetables():
    return render_template('vegetables.html', vegetables_list=["beans", "carrots", "beetroot", "cucumber"])


@app.route("/fruits")
def get_fruits():
    return render_template('fruits.html', fruits_list=["melon", "apple", "strawberry", "grape"])


if __name__ == "__main__":
    app.run(debug=True)
