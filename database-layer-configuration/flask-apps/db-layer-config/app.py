from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@34.105.247.56/flask_db"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
