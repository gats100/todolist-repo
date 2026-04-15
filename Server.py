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


if __name__ == "__main__":
    app.run(debug=True)