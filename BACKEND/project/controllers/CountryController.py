from flask import escape, session,render_template, request, Response, jsonify, make_response, abort, redirect, url_for, json, g
from flask_classful import route
from project import app
from project.core.controller import controller
from project.maria.Countrydb import Countrydb
# from project import alembic

class CountryView(controller):
	def index(self):
		return "OK"

	def getall(self):
		retCountry=[]
		allCountry=Countrydb.query.order_by(Countrydb.nicename).all()
		for country in allCountry:
			tmp = {}
			tmp['id']=country.id
			tmp['nicename']=country.nicename
			# tmp['iso2']=country.iso
			tmp['label']=country.nicename+" ("+country.iso+")"
			retCountry.append(tmp)
		return jsonify(retCountry)