from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

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
  return render_template('home.html', jobs=jobs, company_name="Google")


@app.route('/api/jobs')
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)


if __name__ == "__main__":
  # print("I'm inside")
  app.run(host='0.0.0.0', debug=True)
