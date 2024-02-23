from flask import Flask, request, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import re
import sys

# Check for command-line arguments
if len(sys.argv) != 4:
    print("Usage: python 8-add_retrieve_users.py <db_username> <db_password> <db_name>")
    sys.exit(1)

db_username = sys.argv[1]
db_password = sys.argv[2]
db_name = sys.argv[3]
db_host = 'localhost'

app = Flask(__name__)

# Connect to alx_flask_db
path = 'mysql://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3])
app.config['SQLALCHEMY_DATABASE_URI'] = path

db = SQLAlchemy(app)

#defining user model class

class User(db.Model):
    ''' creating class User that inherits from Model '''
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(128))
    email = db.Column(String(128), unique=True, nullable=False)   


# Create the database tables
def create_tables():
    with app.app_context():
        db.create_all()


create_tables()
# This calls the function to create tables


@app.route("/", strict_slashes=False)
def index():
    return "Hello, ALX Flask!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)