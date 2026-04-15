import uuid
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

lists_store = [
    {"id": "a1", "title": "Einkaufen"},
    {"id": "b2", "title": "Schule"},
    {"id": "c3", "title": "Freizeit"}
]

entries_store = [
    {"id": str(uuid.uuid4()), "title": "Brot", "info": "", "list_id": "a1"},
    {"id": str(uuid.uuid4()), "title": "Hausaufgaben", "info": "", "list_id": "b2"},
    {"id": str(uuid.uuid4()), "title": "Film schauen", "info": "", "list_id": "c3"}
]

@app.after_request
def cors(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, DELETE, PATCH"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response

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



@app.route("/lists/<lid>", methods=["GET", "POST", "DELETE"])
def manage_list(lid):
    current = next((x for x in lists_store if x["id"] == lid), None)

    if current is None:
        abort(404)

    if request.method == "GET":
        result = [e for e in entries_store if e["list_id"] == lid]
        return jsonify(result)

    if request.method == "POST":
        payload = request.get_json(force=True)

        if "title" not in payload:
            abort(400)

        new_item = {
            "id": str(uuid.uuid4()),
            "title": payload["title"],
            "info": payload.get("info", ""),
            "list_id": lid
        }

        entries_store.append(new_item)
        return jsonify(new_item), 201

    if request.method == "DELETE":
        lists_store.remove(current)
        return "", 200


@app.route("/items/<eid>", methods=["PATCH", "DELETE"])
def manage_entry(eid):
    entry = next((x for x in entries_store if x["id"] == eid), None)

    if not entry:
        abort(404)

    if request.method == "PATCH":
        payload = request.get_json(force=True)

        if "title" in payload:
            entry["title"] = payload["title"]

        if "info" in payload:
            entry["info"] = payload["info"]

        return jsonify(entry), 200

    if request.method == "DELETE":
        entries_store.remove(entry)
        return "", 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)