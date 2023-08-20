# code to connect to database and extract data from database. - 2.0.20

from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem",
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(
      text("Select * from jobs")
    )  #any sql query, returns a list of values/tables. ; error is saying we need secure way to connect to DB.
    jobs = []
    for row in result.all():
      jobs.append(dict(row._asdict()))

  return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs where id = {}".format(id)))

    # result = conn.execute(text("select * from jobs where id = 3"))
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0]._asdict())

  # result_all = result.all()
  # print("type(result_all) : ", type(result_all))
  # print("result_all : ", result_all)
  # print("type(result_all[0]) : ", type(result_all[0]))
  # print("result_all[0] : ", result_all[0])
  # # first_result_dict = result_all[0].__dict__
  # first_result = result_all[0]
  # first_result_dict = dict(first_result._asdict())
  # print("first_result_dict",first_result_dict)
  # print("type(first_result_dict)",type(first_result_dict))
