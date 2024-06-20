from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo



app = Flask(__name__)
app.config["SECRET_KEY"]="123"

app.config["MONGO_URI"] = "mongodb+srv://Dinesh:miyuki767%40@dineshdatabase.qrsx5on.mongodb.net/KuroCareersWebsite"
mongo=PyMongo(app)

 

@app. route( "/" )
def helloworld():
    data=mongo.db.jobopenings.find()
    return render_template('home.html',company_name='Kuro',jobs=data)





if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
