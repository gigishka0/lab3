from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)


users = {
    "pasha": "qwerty"
}

def check_auth(username, password):
    return username in users and users[username] == password

def need_auth():
    return jsonify({"error": "auth required"}), 401

def auth_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return need_auth()
        return f(*args, **kwargs)
    return wrapper



items = {
    1: {"type": "GPU", "name": "GTX 1650", "price": 5000},
    2: {"type": "CPU", "name": "Intel i5", "price": 3000},
    3: {"type": "SSD", "name": "SSD 512GB", "price": 1500},
}


@app.route("/items", methods=["GET", "POST"])
@auth_required
def items_handler():
    if request.method == "GET":
        return jsonify(items)

    if request.method == "POST":
        data = request.get_json()
        if not data:
            return jsonify({"error": "json required"}), 400

        new_id = max(items.keys()) + 1 if items else 1
        items[new_id] = data
        return jsonify({"message": "item created", "id": new_id}), 201


@app.route("/items/<int:item_id>", methods=["GET", "PUT", "DELETE"])
@auth_required
def item_handler(item_id):

    if item_id not in items:
        return jsonify({"error": "item not found"}), 404

    if request.method == "GET":
        return jsonify(items[item_id])

    if request.method == "PUT":
        data = request.get_json()
        if not data:
            return jsonify({"error": "json required"}), 400
        items[item_id].update(data)
        return jsonify({"message": "item updated"})

    if request.method == "DELETE":
        del items[item_id]
        return jsonify({"message": "item deleted"})


if __name__ == "__main__":
    app.run(port=8000)
