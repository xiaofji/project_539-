#################
#### imports ####
#################

from flask import redirect, render_template, request, \
    url_for, Blueprint
from flask.ext.login import login_user, login_required, logout_user, current_user

from .forms import LoginForm, RegisterForm
from project import db
from project.models import User, bcrypt

################
#### config ####
################

users_blueprint = Blueprint(
    'users', __name__,
    template_folder='templates'
)


################
#### routes ####
################

@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(username=request.form['username']).first()
            print user
            if user is not None and bcrypt.check_password_hash(
                user.password, request.form['password']
            ):
                login_user(user)
                return redirect(url_for('home.personalpage'))

            else:
                error = 'Invalid username or password.'
    return render_template('login.html', form=form, error=error, user=current_user)




@users_blueprint.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('home.default'))
    return render_template('register.html', form=form, user=current_user)
