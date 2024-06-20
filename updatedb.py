from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo



app = Flask(__name__)
app.config["SECRET_KEY"]="123"

app.config["MONGO_URI"] = "mongodb+srv://Dinesh:miyuki767%40@dineshdatabase.qrsx5on.mongodb.net/KuroCareersWebsite"
mongo=PyMongo(app)

ud_data={
    "email":"add@gmail.com"
}

data=mongo.db.jobopenings.insert_one(ud_data)
print("Data Added")