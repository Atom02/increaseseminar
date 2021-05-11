from wtforms import Form, Field, IntegerField, HiddenField, FormField, BooleanField, StringField, TextAreaField, FieldList, PasswordField, SelectMultipleField, validators, ValidationError

class ParticipantForm(Form):
    id=IntegerField(label="ID")
    email=StringField(label="Email",validators=[validators.email(), validators.required()])
    name=StringField(label="Name",validators=[validators.required()])
    affiliation=StringField(label="Affiliation", validators=[validators.required()])
    uniqueURL=StringField(label="URL",validators=[validators.required()])
    country_id=IntegerField(label="country_id",validators=[validators.required()])

    def setScope(self,scope):
      if scope == "update":
        self.id.validators = [validators.required()]
        # self.oldPassword.validators = [requiredIf("password")]
        # print(type(self.userid.validators[0]).__name__)
    #   if scope == "add":
    #     self.id.validators.append(validators.required())

    def add(self):
        ret = {}
        try:
            pass
        except Exception as e:
            pass
        finally:
            pass
    
    def validate(self):
      status = True
      rv = Form.validate(self)
      if not rv:
        status = False