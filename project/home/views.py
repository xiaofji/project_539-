#################
#### imports ####
#################

from flask import Flask, render_template, Blueprint, request, redirect, url_for, flash
from flask_mail import Message, Mail
from flask.ext.login import login_required, current_user, login_user, logout_user

from project import db, app
from project.models import User, Recipe, Association, Ingre, Recipe_ingre, bcrypt
from .forms import AddRecipeForm, ContactForm
from project.users.forms import LoginForm
import json

mail = Mail()


app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'umsiwebdesign@gmail.com'
app.config["MAIL_PASSWORD"] = '105sstate'
mail.init_app(app)
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
@home_blueprint.route("/index", methods=['GET', 'POST'])
# @login_required
def default():
    form = LoginForm(request.form)
    error = None
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
            return redirect(url_for('users.login'))
        elif request.form['submit'] == 'logout':
            logout_user()
            return render_template("index.html", name = "index", title = "Chinese Cooking", form=form, user=current_user)


    return render_template("index.html", name = "index", title = "Chinese Cooking", error = error, form=form, user=current_user)



@home_blueprint.route("/yuecai/<LearningRecipeName>", methods=['GET', 'POST'])
def yuecai(LearningRecipeName):
    error = None
    ingresobj = Ingre.query.filter(Ingre.recipes.any(recipename=LearningRecipeName)).all()
    ingres = []
    ingresurl = []
    ingresorder = Recipe.query.filter_by(recipename=LearningRecipeName).first().ingresorder.split(" ")
    instruction = Recipe.query.filter_by(recipename=LearningRecipeName).first().instruction.split("|")
    print instruction

    for i in ingresorder:
        for obj in ingresobj:

            if obj.id == int(i):
                ingres.append(obj.ingrename)
                ingresurl.append(obj.url)


    form = LoginForm(request.form)
    formR = AddRecipeForm(request.form)
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
            return redirect(url_for('users.login'))
        elif request.form['submit'] == 'logout':
            logout_user()
            return redirect(url_for("home.default"))
        else:
            user=User.query.filter_by(username=current_user.username).first()
            recipe = Recipe.query.filter_by(recipename=request.form['submit']).first()
            if recipe is not None:
                recipes = Recipe.query.filter(Recipe.users.any(username=current_user.username)).all()

                if recipe not in recipes:
                    user.add_recipes([recipe])

                    # commit the changes
                    db.session.commit()
            return redirect(url_for("home.personalpage"))
    if LearningRecipeName == "sliced_cold_chicken" or LearningRecipeName == "bitter_shrimp_ball" or LearningRecipeName == "sichuan_fish":
        return render_template("yuecai.html", title = "Cooking", form=form, instruction=instruction, user=current_user, error=error, LearningRecipeName = LearningRecipeName, ingres=ingres, ingresurl=ingresurl)
    else:
        return render_template("coming.html", title = "Cooking", form=form, user=current_user, error=error, LearningRecipeName = LearningRecipeName)


# use decorators to link the function to a url
@home_blueprint.route('/personalpage', methods=['GET', 'POST'])
@login_required
def personalpage():
    error = None
    recipes = None
    form = LoginForm(request.form)
    if current_user is None:
        title = 'personalpage'
    else:
        title = current_user.username
    if request.method == 'POST':
        if request.form['submit'] == 'login':
            if form.validate_on_submit():
                user = User.query.filter_by(username=request.form['username']).first()
                print user
                if user is not None and bcrypt.check_password_hash(
                    user.password, request.form['password']
                ):
                    login_user(user)
                    title = user

                else:
                    error = 'Invalid username or password.'
        elif request.form['submit'] == 'signup':
            return redirect(url_for('users.login'))
        elif request.form['submit'] == 'logout':
            logout_user()
            return redirect(url_for('home.default'))

    recipes = Recipe.query.filter(Recipe.users.any(username=current_user.username)).all()
    recipesNotLearnt = Recipe.query.filter(~Recipe.users.any(username=current_user.username)).all()
    recipesname = []
    recipesNotLearntname = []
    for recipe in recipes:
        recipesname.append(recipe.recipename)
    for recipe in recipesNotLearnt:
        recipesNotLearntname.append(recipe.recipename)
    # recipes = db.session.query(Recipe).all()
    # return render_template('personalpage.html', recipes=recipes, recipesNotLearnt = recipesNotLearnt, form=form, user=current_user)  # render a template

    return render_template('personalpage.html', title=title, recipes=recipesname, recipesNotLearnt = recipesNotLearntname, form=form, user=current_user)  # render a template

@home_blueprint.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()
  forml = LoginForm()
  if request.method == 'POST':
    msg = Message(form.subject.data, sender='contact@example.com', recipients=['xiaofji@umich.edu'])
    msg.body = """
      From: %s <%s>
      %s
      """ % (form.name.data, form.email.data, form.message.data)
    mail.send(msg)
    msg_rep = Message("Confirmation", sender='contact@example.com', recipients=[form.email.data])
    msg_rep.body = """
      Thank you for your message!
      """
    mail.send(msg_rep)
    flash("Thank you for sumitting your Message!")
    return redirect(url_for("home.contact"))

  elif request.method == 'GET':
    return render_template('contact.html', form=forml, formc=form)
