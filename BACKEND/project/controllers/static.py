from project import app
from flask import Response,send_file,abort
import os
# YOUR STATIC FILES IS CONFIGURE HERE
@app.route('/static/<path:filename>')
def custom_static(filename):
	# fl = os.path.join(app.root_path,'static',filename)
	# if os.path.isfile(fl):
	# 	# return send_file(fl)
	# 	return send_from_directory(fl,filename)
	# else:
	# 	abort(404)
	fl = os.path.join(app.root_path,'static')
	return send_from_directory(fl,filename)