from flask import Flask, jsonify

from src.thirdparty.postgresql import db

app=Flask(__name__)

_db = db()

@app.route("/", methods=["GET"])
def get_all_meals():
    meals = _db.select("meal")
    return jsonify({"result":meals})