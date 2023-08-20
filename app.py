from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_db

app = Flask(__name__)

# JOBS = [
#   {
#     'id': 1,
#     'title': 'Software Engineer',
#     'location': 'USA',
#     'salary': '$150,000',
#   },
#   {
#     'id': 2,
#     'title': 'Backend Engineer',
#     'location': 'USA',
#     'salary': '$250,000',
#   },
#   {
#     'id': 3,
#     'title': 'Frontend Engineer',
#     'location': 'USA',
#   },
# ]


@app.route("/")
def hello():
  jobs = load_jobs_from_db()
  # return render_template('home.html', jobs=jobs, company_name="Google")
  return render_template('home.html', jobs=jobs)


@app.route('/api/jobs')
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)


@app.route('/job/<id>')
def show_job(id):
  job = load_job_from_db(id)

  if job is None:
    return "<!DOCTYPE html><html><head><title>Not Found</title></head><body><h1>404 : Page Not Found</h1></body></html>"

  return render_template('jobpage.html', job=job)


if __name__ == "__main__":
  # print("I'm inside")
  app.run(host='0.0.0.0', debug=True)
