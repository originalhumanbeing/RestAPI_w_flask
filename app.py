from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


stores = [{
        'name': 'My Store',
        'items': [{'name': 'my item', 'price': 15.99}]
    }]


@app.route('/')
def home():
    return render_template('index.html')

#post /store data: {name :}
@app.route('/store')
def create_store():
    request_date = request.get_json()
    new_store = {
        'name': request_date['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

#get /store/<name> data: {name: }
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'msg': 'store not found'})


if __name__ == '__main__':
    app.run()
