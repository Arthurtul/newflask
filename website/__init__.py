from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "skdjsfgkg"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////Users/arturkryzanovskij/PycharmProjects/newflask/website/models/data.sqlite"
    db.init_app(app)
    # print(app.config['SQLALCHEMY_DATABASE_URI'])

    with app.app_context():
        db.create_all()

    from.views import views
    from.auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app
