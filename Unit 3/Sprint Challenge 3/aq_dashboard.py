"""OpenAQ Air Quality Dashboard with Flask."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from openaq import OpenAQ

app = Flask(__name__)
api = OpenAQ()

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
DB = SQLAlchemy(app)


class Record(DB.Model):
    # id (integer, primary key)
    id = DB.Column(DB.Integer, primary_key=True)
    # datetime (string)
    datetime = DB.Column(DB.String)
    # value (float, cannot be null)
    value = DB.Column(DB.Float, nullable=False)

    def __repr__(self):
        return f'Time: {self.datetime} --- Value: {self.value}'


def get_results():
    status, body = api.measurements(city='Los Angeles', parameter='pm25')
    new_list = []
    for i in body['results']:
        new_list.append((i["date"]["utc"], i["value"]))
    return new_list


@app.route('/')
def root():
    """Base view."""
    return str(Record.query.filter(Record.value >= 18).all())


@app.route('/refresh')
def refresh():
    """Pull fresh data from Open AQ and replace existing data."""
    DB.drop_all()
    DB.create_all()
    new_list = get_results()
    i = 1
    for date, value in new_list:
        new = Record(id=i, datetime=date, value=value)
        DB.session.add(new)
        i = i+1

    DB.session.commit()
    return 'Data refreshed!'
