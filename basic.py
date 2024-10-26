from flask import (Flask, render_template, redirect, 
                   url_for,request, session, flash, send_file, jsonify)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import datetime


app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
app.config["MONGO_URI"] = "mongodb://localhost:27017/flask_database"

mongo = PyMongo(app)
db = mongo.db

@app.route('/')
def home():

    return render_template('home.html')



if __name__ == '__main__':
    app.run(debug=True)
