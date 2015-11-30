from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo



class AddRecipeForm(Form):
    recipename = TextField('recipename', validators=[DataRequired()])
