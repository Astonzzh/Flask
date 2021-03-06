from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://localhost:3306/accounts'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "123"
db = SQLAlchemy(app)
pymysql.install_as_MySQLdb()
db.create_all()


class Account(db.Model):
    # id = db.Column(db.INT, autoincrement=True, nullable=False)
    username = db.Column(db.VARCHAR(20), primary_key=True, nullable=False, index=True)
    password = db.Column(db.VARCHAR(100), nullable=False)


@app.route('/')
def hello_world():
    return "hello world"


import auth
app.register_blueprint(auth.bp)


if __name__ == '__main__':
    app.run()
