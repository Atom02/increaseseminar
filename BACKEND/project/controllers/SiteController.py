from flask import escape, session,render_template, request, Response, jsonify, make_response, abort, redirect, url_for, json, g
from flask_classy import route
from flask_restful import Api, Resource
from project import app
from app.mongoController import mongoController
from project.models.UserModel import User
import pprint
from mongoengine.errors import ValidationError

class SiteView(mongoController):
	def index(self):
		# nuser = User()
		# nuser.name = "Candra Nur Ihsan"
		# nuser.email = "candra.nurihsan9"
		# try:
		# 	nuser.save()
		# except ValidationError as e:
		# 	print(type(e))
		# except mongoengine.errors.ValidationError as e:
		# 	# print(type(e[0]))
		# 	pprint.pprint(e.to_dict())
		# 	print(e.to_dict())
		return "Forbiden To Come Here", 403

	