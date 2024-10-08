from flask import Flask, url_for, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'HGAVBKIAHA^*uJHJcfgghgy167W17GHS'

@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('index.html')

@app.route('/special_gift_combos', methods=['POST', 'GET'])
def special_gift_combos():
    return render_template('pages/special_gift_combos.html')

@app.route('/customized_items', methods=['POST', 'GET'])
def customized_items():
    return render_template('pages/customized_items.html')

@app.route('/all_products', methods=['POST', 'GET'])
def all_products():
    return render_template('pages/all_products.html')

@app.route('/new_on_sale', methods=['POST', 'GET'])
def new_on_sale():
    return render_template('pages/new_on_sale.html')

@app.route('/about', methods=['POST', 'GET'])
def about():
    return render_template('pages/about.html')

@app.route('/help', methods=['POST', 'GET'])
def help():
    return render_template('pages/help.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('errors/500.html'), 500