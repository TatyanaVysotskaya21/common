from flask import Flask, render_template
from utils import get_data

app = Flask(__name__)


@app.route('/')
def get_home_page():
    title = "Home"
    return render_template("home.html", title=title)


@app.route('/<name_product>')
def get_name_product(name_product):
    for product in get_data():
        if product["title"] == name_product:
            return render_template("base.html",
                                   title=product["title"],
                                   text=product["text"],
                                   img=product["img"],
                                   text_length=len(product["text"]))
    else:
        return render_template("error_tab.html")


@app.route('/author')
def get_author():
    title = "Author"
    return render_template("author.html", title=title)


if __name__ == "__main__":
    app.run(debug=True)
