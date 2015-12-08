from flask_wtf import Form
from wtforms import TextField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from wtforms.fields.html5 import EmailField


class AddRecipeForm(Form):
    recipename = TextField('recipename', validators=[DataRequired()])

class ContactForm(Form):

  name = TextField("Name")
  email = EmailField("Email")
  subject = TextField("Subject")
  message = TextAreaField("Message")
  submit = SubmitField("Send")
  
