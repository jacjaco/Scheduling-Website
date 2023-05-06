from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    fname = db.Column(db.String(100))
    lname = db.Column(db.String(100))

    def __repr__(self):
        return f"<User user_id={self.id} email={self.email}>"

def connect_to_db(flask_app, db_uri="postgresql:///students", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)
    # db.create_all()
    print("Connected to the db!")

if __name__ == "__main__":
    # from flask import Flask

    # app = Flask(__name__)
    from server import app
    connect_to_db(app)
