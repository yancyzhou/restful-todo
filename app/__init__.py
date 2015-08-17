from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from config import config
from flask.ext.restful import Api,Resource,reqparse
bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()

def create_app(config_name):
  app = Flask(__name__)
  api = Api(app)
  app.config.from_object(config[config_name])
  config[config_name].init_app(app)

  bootstrap.init_app(app)
  moment.init_app(app)
  db.init_app(app)

  from app.main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  return app
