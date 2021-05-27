# -*- coding: utf-8 -*-
__version__ = '0.1'
from flask import Flask,redirect,url_for
from flask_socketio import SocketIO
from flask_mobility import Mobility
from flask_session import Session
from flask_caching import Cache
from flask_wtf.csrf import CSRFProtect
from datetime import timedelta
from flask_cors import CORS
from flask_mail import Mail
# from flask_mongoengine import MongoEngine
from flask_sqlalchemy import SQLAlchemy
# from flask_alembic import Alembic
from flask_migrate import Migrate
from flask_cors import CORS, cross_origin
import types
import os

import project.appConfig as cfgP
import project.appConfigLocal as cfgLocal
# cfgTmp = [a for a in dir(cfgP) if not a.startswith('__')]
# cfg = types.SimpleNamespace()
# for c in cfgTmp:
# 	setattr(cfg,c,getattr(cfgP,c))
# 	if hasattr(cfgLocal, c):
# 		setattr(cfg,c,getattr(cfgLocal,c))
# print('cfg',cfg)

app = Flask('project')


# cors = CORS(app, resources={r"/*": {"origins": "http://localhost:8080, http://127.0.0.1:8080"}})

app.secret_key = 'oz@vZZ&IFICRSqg(WSU.CmM:#w=y8urxfV'

app.config["NAME"]="INCREASE"
app.config['SECRET_KEY'] = app.secret_key
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024 #32 Mega
app.config['CACHE_KEY_PREFIX']='kamajaya2021'
app.config["CACHE_TYPE"]="simple"
app.config["CACHE_DEFAULT_TIMEOUT"]=600
app.config["CACHE_THRESHOLD"]=1000
app.config["SESSION_TYPE"]="filesystem"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=31)
app.config['SESSION_PERMANENT'] = True 

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config["ALLOWED_EXTENSIONS"] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

# app.config['CORS_HEADERS'] = 'Content-Type'
app.config['CORS_ORIGINS'] = "*"
# app.config['MONGODB_SETTINGS'] = cfg.mongodb

app.config['SQLALCHEMY_DATABASE_URI'] = cfgLocal.mariadb
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ENGINE_OPTIONS']={ "pool_pre_ping" : True}
app.config['DEBUG'] = cfgLocal.appdebug

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config["ALLOWED_EXTENSIONS"] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['CORS_SUPPORTS_CREDENTIALS'] = True

app.config['MAIL_SERVER']='mail.lapan.go.id'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='increase@lapan.go.id'
app.config['MAIL_PASSWORD']='1Ncre@se'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# app.debug = True
app.jinja_env.add_extension("project.helper.JinjaExt.RelativeInclude")
app.jinja_env.add_extension("jinja2.ext.do")

mail = Mail(app)
csrf = CSRFProtect(app)
Mobility(app)
socketio = SocketIO(app, cors_allowed_origins = ["*"])
cache = Cache(app)
# mongodb = MongoEngine(app)
mariadb = SQLAlchemy(app)
migrate = Migrate(app, mariadb)
# api_v1_cors_config = {
	# "origins":"*"
#   "origins": ["http://localhost:8080","http://127.0.0.1:8080"]
# }
# cors = CORS(app, resources={r"/*": api_v1_cors_config})
CORS(app)
print(CORS)

from project.maria import Countrydb
from project.maria import Peserta
from project.maria import Participant
# alembic = Alembic()
# alembic.init_app(app)

from project.controllers import *
SiteController.SiteView.register(app)
CountryController.CountryView.register(app)
PesertaController.PesertaView.register(app)