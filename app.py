from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Software Engineer',
    'location': 'USA',
    'salary': '150000',
  },
  {
    'id': 2,
    'title': 'Backend Engineer',
    'location': 'USA',
    'salary': '250000',
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


if __name__ == "__main__":
  # print("I'm inside")
  app.run(host='0.0.0.0', debug=True)
