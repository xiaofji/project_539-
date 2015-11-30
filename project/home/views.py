#################
#### imports ####
#################

from flask import render_template, Blueprint, request, redirect, url_for
from flask.ext.login import login_required, current_user, login_user, logout_user

from project import db
from project.models import User, Recipe, Association, Ingre, Recipe_ingre, bcrypt
from .forms import AddRecipeForm
from project.users.forms import LoginForm

################
#### config ####
################

home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)


################
#### routes ####
################
@home_blueprint.route("/", methods=['GET', 'POST'])
# @login_required
def default():
    form = LoginForm(request.form)
    if request.method == 'POST':
        if request.form['submit'] == 'login':
            if form.validate_on_submit():
                user = User.query.filter_by(username=request.form['username']).first()
                print user
                if user is not None and bcrypt.check_password_hash(
                    user.password, request.form['password']
                ):
                    login_user(user)

                else:
                    error = 'Invalid username or password.'
        elif request.form['submit'] == 'signup':
            return redirect(url_for('users.register'))
        elif request.form['submit'] == 'logout':
            logout_user()
            return render_template("index.html", name = "index", title = "WELCOME", form=form, user=current_user)


    return render_template("index.html", name = "index", title = "WELCOME", form=form, user=current_user)

@home_blueprint.route("/index")
def index():
    return render_template("index.html", name = "index", title = "WELCOME")

@home_blueprint.route("/yuecai")
def yuecai():
    return render_template("yuecai.html", name = "yuecai", title = "YUECAI")
# use decorators to link the function to a url
@home_blueprint.route('/personalpage', methods=['GET', 'POST'])
@login_required
def personalpage():
    # return "Hello, World!"  # return a string
    # form = LoginForm(request.form)
    # user = User.query.filter_by(username=request.form['username']).first()
    form = AddRecipeForm(request.form)

    if request.method == 'POST':
        if form.validate_on_submit():
            user=User.query.filter_by(username=current_user.username).first()
            recipe = Recipe.query.filter_by(recipename=request.form['recipename']).first()
            if recipe is not None:
                recipes = Recipe.query.filter(Recipe.users.any(username=current_user.username)).all()

                if recipe not in recipes:
                    user.add_recipes([recipe])

                    # commit the changes
                    db.session.commit()

    recipes = Recipe.query.filter(Recipe.users.any(username=current_user.username)).all()
    # recipes = db.session.query(Recipe).all()
    return render_template('personalpage.html', recipes=recipes, form=form, user=current_user)  # render a template

    # posts = db.session.query(BlogPost).all()
    # return render_template('index.html', posts=posts)  # render a template


@home_blueprint.route('/welcome')
def welcome():
    return render_template('welcome.html', user=current_user)  # render a template
