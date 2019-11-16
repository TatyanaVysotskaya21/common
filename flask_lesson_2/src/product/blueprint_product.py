import os
import uuid

from flask import Blueprint, render_template, request, session, url_for
from werkzeug.utils import secure_filename, redirect

from src.model import AddProductForm
from src.utils import get_data, add_data

product = Blueprint("product", __name__, template_folder='template')

I_AM_CONSTANT = 'product.json'
path_img = 'static'


@product.route("/products", methods=['POST', 'GET'])
def get_products():
    get_dict = {'GET': render_template('all_products.html', data=get_data(I_AM_CONSTANT)),
                'POST': "redirect(url_for('products?price=<price>', price=request.form.get('price')))"}
    return get_dict.get(request.method)


@product.route("/add_product", methods=['POST', 'GET'])
def add_product():
    form = AddProductForm()
    return render_template("add_product.html", form=form)


@product.route('/submit', methods=['POST'])
def save_product():

    try:
        price = int(request.form.get('price'))
    except ValueError:
        return redirect(url_for('product.add_product'))

    if price > 0:
        dict_product = {'id': str(uuid.uuid4()),
                        'name': request.form.get('name'),
                        'description': request.form.get('description'),
                        'price': price,
                        'img_name': upload_image()}

        data = get_data(I_AM_CONSTANT)
        data.append(dict_product)
        add_data(data, I_AM_CONSTANT)
        return render_template('all_products.html', data=get_data(I_AM_CONSTANT))
    else:
        return redirect(url_for('product.add_product'))


@product.route('/upload', methods=['POST'])
def upload_image():
    f = request.files['img_name']
    filename = secure_filename(f.filename)
    f.save(os.path.join(path_img, filename))
    return filename


@product.route('/products/<info_product>')
def product_page(info_product):
    for prod in get_data(I_AM_CONSTANT):
        if prod['name'] == info_product or prod['id'] == info_product:
            session[info_product] = True
            return render_template('product.html',
                                   title=prod["name"],
                                   description=prod['description'],
                                   img=prod['img_name'],
                                   price=prod['price'])
    else:
        return render_template('error_404.html')
