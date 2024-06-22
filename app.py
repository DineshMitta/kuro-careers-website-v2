from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from pymongo import MongoClient

app = Flask(__name__)
app.config["SECRET_KEY"]="123"
app.config["MONGO_URI"] = "mongodb+srv://Dinesh:miyuki767%40@dineshdatabase.qrsx5on.mongodb.net/KuroCareersWebsite?retryWrites=true&w=majority"

mongo=PyMongo(app)





@app. route( "/" )
def helloworld():
    jobs = list(mongo.db.jobopenings.find())
    for job in jobs:
        job['_id'] = str(job['_id'])  # Convert ObjectId to string for JSON serialization
    return render_template('home.html', company_name='Kuro', jobs=jobs)


def load_job_by_id(job_id):
     
     job = mongo.db.jobopenings.find_one({'_id': ObjectId(job_id)})
     if job is None:
        return None
     else:
        # Convert the MongoDB document to a dictionary
        job['_id'] = str(job['_id'])  # Convert ObjectId to string for JSON serializability
        return job


@app.route("/api/jobs")
def list_jobs():
    data=mongo.db.jobopenings.find()
    jobs = list(data)
    print(jobs)
    for job in jobs:
        job['_id'] = str(job['_id'])  # Convert ObjectId to string for JSON serialization
    return jsonify(jobs)


@app.route("/api/job/<string:id>")
def show_job(id):
    
    job = load_job_by_id(id)
    if job:
        return render_template('jobpage.html', job=job)
    else:
        return jsonify({"message": "Job not found"}), 404




if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
