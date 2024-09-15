import os
from flask import Flask
from flask_session import Session
from extensions import db
from application.blueprints.home import home
from application.blueprints.auth import auth
from application.blueprints.book import book

from flask_migrate import Migrate

app = Flask(__name__, template_folder=os.path.abspath('application/templates'))

app.config.from_pyfile('config.py')

Session(app)

db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(home)
app.register_blueprint(auth)
app.register_blueprint(book)


if __name__ == '__main__':
    app.run(debug=True)