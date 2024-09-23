import os
from flask import Flask
from app.routes import configure_routes
from flask_restx import Api
from app.config import CONECTION_URI
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']=CONECTION_URI
    api = Api(app, version='1.0', title='Country API',doc='/swagger/')
    configure_routes(api)
    from app.db import db
    db.init_app(app)
    from app.models.country import Country
    with app.app_context():
        db.create_all()
    return app



if __name__ == "__main__":
    app = create_app()
    print("Starting API...")
    app.run(host="0.0.0.0", port=8080)