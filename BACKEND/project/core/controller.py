from flask_classful import FlaskView
from flask import render_template,url_for,abort,g,make_response,Response
from project import app
from flask_wtf.csrf import generate_csrf

class controller(FlaskView):
    connectDb = True
    defAcl = {
        "allow" : True,
        "action": "*",
        "matchCallback":None,
        "denyCallback":None,
        "roles": "*"
    }
    # aclDB = None
    layout = None
    pagedata = {}
    def before_request(self, name, *args, **kwargs):
        pass

    def after_request(self, name, resp):
        # if hasattr(g,"db") and g.db.db is not None:
        #     g.db.close()
        csrf=generate_csrf()
        resp.set_cookie('CSRF-TOKEN', csrf)
        # print(csrf)
        return resp

    def render(self,page,data={}):
        pagedata = {}
        pagedata["pagedata"] =self.pagedata
        z = {**pagedata,**data}
        resp = make_response(render_template(page,**z))
        # csrf=generate_csrf()
        # resp.set_cookie('CSRF-TOKEN', csrf)
        return resp