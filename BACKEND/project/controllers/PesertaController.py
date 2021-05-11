from flask import escape, session,render_template, request, Response, jsonify, make_response, abort, redirect, url_for, json, g
from flask_classful import route
from flask_mail import Message
from project import app, mariadb, mail
from project.core.controller import controller
import secrets
import re
from project.maria.Participant import Participant
from project.maria.Countrydb import Countrydb
import traceback
from sqlalchemy import exc

class PesertaView(controller):
	def index(self):
		return "OK"

	@route('/register', methods=['POST'])
	def doregister(self):
		ret = {}
		try:
			req = request.form
			url = secrets.token_urlsafe(16)
			pes = Participant()
			pes.name = req.get('name')
			pes.email = req.get('email')
			pes.affiliation = req.get('affiliation')
			pes.country_id = req.get('nationality')
			pes.uniqueURL = url
			print("ALL GOO1")
			mariadb.session.add(pes)
			mariadb.session.flush()
			print("ALL GOO2")
			# updateURL
			upes = Participant.query.get(pes.id)
			print("ALL GOO3",upes.uniqueURL,pes.id)
			upes.uniqueURL = upes.uniqueURL+"_"+str(pes.id)
			print("ALL GOO4")
			ret['status']=True
			print("ALL GOO5")
			# print('peserta',pes.id, pes.uniqueURL)
		
			# traceback.print_exc()
			# except exc.IntegrityError as err:
			# 	print("ERROR 1",err)
			# 	mariadb.session.rollback()
			# 	ret['status']=False
			
			# do send mail
			print("SENDDING EMAIL")
			msg = Message(subject='REGISTRATION CONFRIMATION',sender='noreply@lapan.go.id', recipients=[upes.email])
			data={}
			data['name']=upes.name
			data['affiliation']=upes.affiliation
			country = Countrydb.query.get(upes.country_id)
			data['country']=country.nicename
			msg.body = render_template('register.txt', **data)
			mail.send(msg)


			print("COMMITING DB")
			mariadb.session.commit()

		except exc.IntegrityError as err:
			print('integrityError')
			# print(err.args)
			if re.match("(.*)Duplicate entry(.*)for key 'email'(.*)", err.args[0]):
				ret['errors']={'email':'Email Already Registered'}

			mariadb.session.rollback()
			ret['status']=False
		except Exception as e:
			ret['status']=False
			print("ERROR 3")
			traceback.print_exc()
		finally:
			return jsonify(ret)