from flask_classy import FlaskView
from project import app
from flask import render_template,url_for,abort,g,make_response

from app.RequestRedirect import RequestRedirect
# from app.User import User
class mongoController(FlaskView):
    connectDb = True
    # acl = {
    #     "DB":app.config["DB"],
    #     "denyCallback":(lambda x,y: abort(403)),
    #     "rules":[]
    # }
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

    def after_request(self, name, response):
        # if hasattr(g,"db") and g.db.db is not None:
        #     g.db.close()
        
        return response

    def render(self,page,data={}):
        pagedata = {}
        pagedata["pagedata"] =self.pagedata
        z = {**pagedata,**data}
        resp = make_response(render_template(page,**z))
        return resp