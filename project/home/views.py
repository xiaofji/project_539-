#################
#### imports ####
#################

from flask import render_template, Blueprint, request
from flask.ext.login import login_required, current_user

from project import db
from project.models import User, Recipe, Association, Ingre, Recipe_ingre
from .forms import AddRecipeForm

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

# use decorators to link the function to a url
@home_blueprint.route('/', methods=['GET', 'POST'])
@login_required
def home():
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
    return render_template('index.html', recipes=recipes, form=form)  # render a template

    # posts = db.session.query(BlogPost).all()
    # return render_template('index.html', posts=posts)  # render a template


@home_blueprint.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template
