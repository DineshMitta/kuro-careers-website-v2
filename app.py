from flask import Flask, render_template, jsonify, request
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
        return render_template('jobpage.html', company_name='Kuro', job=job)
    else:
        return jsonify({"message": "Job not found"}), 404






def add_job_application(job_id, application):
    """
    Insert a job application into the MongoDB collection.
    """
    application_data = {
        "job_id": ObjectId(job_id),
        "full_name": application.get("full_name"),
        "email": application.get("email"),
        "linkedin_url": application.get("linkedin_url"),
        "education": application.get("education"),
        "experience": application.get("experience"),
        "resume_url": application.get("resume_url")
    }
    result = mongo.db.jobopenings.insert_one(application_data)
    return str(result.inserted_id)

@app.route("/api/job/<id>/apply", methods=["POST"])
def apply_to_job(id):
    """
    Endpoint to apply for a job.
    """
    data = request.form
    job = load_job_by_id(id)
    if not data:
        return jsonify({"error": "No application data provided"}), 400
    
    application_id = add_job_application(id, data)
    return render_template('application_submitted.html',application=data, job=job)


@app.route("/login/")
def login_user():
    return render_template('login.html')


@app.route("/register/")
def register_user():
    return render_template('register.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
    


    