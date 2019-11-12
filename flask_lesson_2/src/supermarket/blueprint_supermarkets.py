import os
import uuid

from flask import Blueprint, render_template, redirect, request, url_for, session
from werkzeug.utils import secure_filename

from src.model import AddMarketForm
from src.utils import get_data, add_data

markets = Blueprint("markets", __name__, template_folder='template', static_folder='static')

json_file = 'src/supermarket/markets.json'
path_img = '/home/k426/GitHub_repos/common/flask_lesson_2/src/static'


@markets.route("/supermarkets")
def get_supermarkets():
    get_dict = {'GET': render_template('all_markets.html', data=get_data(json_file)),
                'POST': "redirect(url_for('products?location=<location>', location=request.form.get('location')))"}
    for key in get_dict:
        if request.method == key:
            return get_dict.get(key)


@markets.route("/add_market", methods=['POST', 'GET'])
def add_market():
    form = AddMarketForm()
    return render_template("add_market.html", form=form)


@markets.route('/sup_submit', methods=['POST'])
def save_market():
    d = {'id': str(uuid.uuid4()), 'name': request.form.get('name'), 'img_name': upload_image(),
         'location': request.form.get('location')}

    data = get_data(json_file)
    data.append(d)
    add_data(data, json_file)
    return render_template('all_markets.html', data=get_data(json_file))


@markets.route('/upload', methods=['POST'])
def upload_image():
    if request.method == 'POST':
        f = request.files['img_name']
        filename = secure_filename(f.filename)
        f.save(os.path.join(path_img, filename))
        return filename


@markets.route('/supermarkets/<market>')
def market_page(market):
    for i in get_data(json_file):
        if i['name'] == market or i['id'] == market:
            session[market] = True
            return render_template('market.html',
                                   title=i["name"],
                                   location=i["location"],
                                   img=i['img_name'])
    else:
        return render_template('error_404.html')
