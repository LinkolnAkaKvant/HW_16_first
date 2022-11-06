from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config['JSON_AS_ASCII'] = False
db = SQLAlchemy(app)



