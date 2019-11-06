import os
import uuid

from flask import Blueprint, render_template, redirect, request, url_for, session
from werkzeug.utils import secure_filename


from src.model import AddProductForm
from src.utils import get_data, add_data

product = Blueprint("product", __name__, template_folder='template', static_folder='static')

json_file = 'product.json'
path_img = '/home/k426/GitHub_repos/common/flask_lesson_2/src/static'


@product.route("/products",  methods=['POST', 'GET'])
def get_products():
    if request.method == 'GET':
        return render_template('all_products.html', data=get_data(json_file))
    elif request.method == 'POST':
        return redirect(url_for('products?price=<price>', price=request.form.get('price')))


@product.route("/add_product", methods=['POST', 'GET'])
def add_product():
    form = AddProductForm()
    return render_template("add_product.html", form=form)


@product.route('/submit', methods=['POST'])
def save_product():

    d = {'id': str(uuid.uuid4()), 'name': request.form.get('name'), 'description': request.form.get('description'),
         'price': request.form.get('price'), 'img_name': upload_image()}

    data = get_data(json_file)
    data.append(d)
    add_data(data, json_file)
    return render_template('all_products.html', data=get_data(json_file))


@product.route('/upload', methods=['POST'])
def upload_image():
    if request.method == 'POST':
        f = request.files['img_name']
        filename = secure_filename(f.filename)
        f.save(os.path.join(path_img, filename))
        return filename


@product.route('/products/<info_product>')
def product_page(info_product):
    for prod in get_data(json_file):
        if prod["name"] == info_product or prod['id'] == info_product:
            session[info_product] = 'visited_page'
            return render_template('product.html',
                                   title=prod["name"],
                                   description=prod['description'],
                                   img=prod['img_name'],
                                   price=prod['price'])
    else:
        return render_template('error_404.html')

