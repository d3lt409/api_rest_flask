from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tree.db"
# initialize the app with the extension
db.init_app(app)

    
with app.app_context():
    
    import routes
    db.create_all()


    
