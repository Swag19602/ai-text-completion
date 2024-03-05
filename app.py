from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from os import path, getcwd, environ
from models.users import Users
from models.chat_logs import ChatLogs
from config import db, SECRET_KEY
from routes.chat_api import event_bp

# Load environment variables from .env file
load_dotenv(path.join(getcwd(), '.env'))


def create_app():
    global db
    app = Flask(__name__)

    # Configure SQLite database 
    app.config["SQLALCHEMY_DATABASE_URI"] = environ.get('DB_URI')
    app.config["SQLALCHEMY_ECHO"] = False
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_MAX_OVERFLOW"] = 1000
    app.config["SQLALCHEMY_POOL_SIZE"] = 100
    app.secret_key = SECRET_KEY
    app.secret_key = SECRET_KEY

    # Initialize database with the app
    db.init_app(app)
    print("DB Initialized Successfully")

    # Enable CORS for your Flask app
    CORS(app)

    #import the blueprint 
    app.register_blueprint(event_bp)

    # Create database tables
    with app.app_context():
        # db.drop_all()
        db.create_all()
        db.session.commit()

    return app


if __name__ == "__main__":
    # Call create_app to get the Flask app
    app = create_app()
    app.run(debug=True)
