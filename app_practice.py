from flask import Flask, jsonify, request, render_template

# app = Flask(__name__)

stores = [
    {
        'name': 'My Store',
        'items': [{'name': 'my item', 'price': 15.99}]
    }
]


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
    for store in stores:
        if store['name'] == name:
            # store['items'].append(request_data)
            # request_data를 바로 넣지 않음 -> 무엇을 보내줄지 확신할 수 없고, 원하지 않는 정보가 포함되어 있을 수도 있으므로
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})

#get /store/<name>/item data: {name :}
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store['items'])
    return jsonify({'message': 'item not found'})


# if __name__ == '__main__':
#     app.run()
