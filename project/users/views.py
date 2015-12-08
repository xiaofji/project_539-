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
@users_blueprint.route('/register', methods=['GET', 'POST'])
def login():
    formr = RegisterForm(request.form)
    forms = LoginForm(request.form)

    error = None

    if request.method == 'POST':
            if request.form['submit'] == 'login':
                if forms.validate_on_submit():
                    user = User.query.filter_by(username=request.form['username']).first()
                    print user
                    if user is not None and bcrypt.check_password_hash(
                        user.password, request.form['password']
                    ):
                        login_user(user)
                        return redirect(url_for('home.personalpage'))
                    else:
                        error = 'Invalid username or password.'
            elif request.form['submit'] == 'signup':
                if formr.validate_on_submit():
                    user = User(
                        username=formr.username.data,
                        password=formr.password.data
                    )
                    db.session.add(user)
                    db.session.commit()
                    login_user(user)
                    return redirect(url_for('home.default'))

    return render_template('register.html', formr=formr, form=forms, user=current_user)
