from flask import Flask
from flaskext.mysql import MySQL
from flask_bcrypt import Bcrypt
from config import Config
from app import routes

app = Flask(__name__)
db = MySQL(app)
bcrypt = Bcrypt(app)
app.config.from_object(Config)
