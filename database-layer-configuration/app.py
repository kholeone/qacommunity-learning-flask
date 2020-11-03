from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:database@34.105.222.230/stand_alone"

db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True)
