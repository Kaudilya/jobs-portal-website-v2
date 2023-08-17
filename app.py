from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Software Engineer',
    'location': 'USA',
    'salary': '$150,000',
  },
  {
    'id': 2,
    'title': 'Backend Engineer',
    'location': 'USA',
    'salary': '$250,000',
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'USA',
  },
]


@app.route("/")
def hello():
  return render_template('home.html', jobs=JOBS, company_name="Google")


@app.route('/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  # print("I'm inside")
  app.run(host='0.0.0.0', debug=True)
