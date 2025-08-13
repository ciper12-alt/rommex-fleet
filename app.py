from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rommex_fleet.db'
app.config['UPLOAD_FOLDER'] = 'uploads'
db = SQLAlchemy(app)

from models import *

@app.route('/')
def index():
    vehicles = Vehicle.query.all()
    return render_template('index.html', vehicles=vehicles)

if __name__ == '__main__':
    if not os.path.exists('rommex_fleet.db'):
        db.create_all()
    app.run(debug=True)
