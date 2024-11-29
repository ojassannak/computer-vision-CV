from flask import Flask, jsonify, request

app = Flask(__name__)


data_store = {
    1: {"Akash": "02", "City": "Shrigonda"},
    2: {"Venky": "08", "City": "Jalgoan"},
    3: {"Rahul": "04", "City": "Pune"},
    4: {"Priya": "01", "City": "Nashik"},
    5: {"Suresh": "05", "City": "Mumbai"},
    6: {"Ojas": "06", "City": "Ratnagiri"},
}

# GET all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data_store)

# GET a single item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = data_store.get(item_id)
    if item:
        return jsonify(item)
    return jsonify({"error": "Item not found"}), 404

# POST a new item
@app.route('/items', methods=['POST'])
def create_item():
    new_item = request.json
    item_id = max(data_store.keys()) + 1 if data_store else 1
    data_store[item_id] = new_item
    return jsonify({"message": "Item created", "item_id": item_id}), 201

# PUT to update an item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    if item_id in data_store:
        updated_data = request.json
        data_store[item_id].update(updated_data)
        return jsonify({"message": "Item updated"})
    return jsonify({"error": "Item not found"}), 404

# DELETE an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id in data_store:
        del data_store[item_id]
        return jsonify({"message": "Item deleted"})
    return jsonify({"error": "Item not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
