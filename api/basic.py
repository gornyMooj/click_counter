from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo
import os


app = Flask(__name__)

app.config['SECRET_KEY']  = os.getenv("SECRET_KEY")
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)
db = mongo.db

@app.route('/')
def home():
    # Fetch the current counter value from the database
    counter_doc = db.counters.find_one({"name": "click_counter"})

    # If the counter doesn't exist, initialize it
    if counter_doc is None:
        db.counters.insert_one({"name": "click_counter", "counter": 1})
        counter_value = 1
    else:
        counter_value = counter_doc["counter"]

    # Pass the counter value to the template
    return render_template('home.html', counter=counter_value)

@app.route('/update_counter', methods=['POST'])
def update_counter():
    # Increment the counter in MongoDB
    db.counters.update_one(
        {"name": "click_counter"},
        {"$inc": {"counter": 1}}
    )

    # Fetch the updated counter value to send back to the frontend
    counter_doc = db.counters.find_one({"name": "click_counter"})
    updated_counter = counter_doc["counter"]

    return jsonify({"counter": updated_counter})

if __name__ == '__main__':
    app.run(debug=True)
