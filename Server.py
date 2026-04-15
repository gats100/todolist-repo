from flask import Flask, jsonify

app = Flask(__name__)

lists_store = [
    {"id": "a1", "title": "Einkaufen"},
    {"id": "b2", "title": "Schule"},
    {"id": "c3", "title": "Freizeit"}
]


@app.route("/lists", methods=["GET"])
def show_lists():
    return jsonify(lists_store), 200

@app.route("/lists", methods=["GET"])
def show_lists():
    return jsonify(lists_store), 200


@app.route("/lists", methods=["POST"])
def create_list():
    payload = request.get_json(force=True)

    if not payload or "title" not in payload:
        abort(400)

    created = {
        "id": str(uuid.uuid4()),
        "title": payload["title"]
    }

    lists_store.append(created)
    return jsonify(created), 201

if __name__ == "__main__":
    app.run(debug=True)