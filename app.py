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
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
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
    return jsonify({'message': 'store not found'})

#get /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

#post /store/<name> data: {name :}
@app.route('/store/<string:name>/item' , methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    return jsonify(request_data)

#get /store/<name>/item data: {name :}
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    pass


if __name__ == '__main__':
    app.run()
