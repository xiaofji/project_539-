from project import db
from project.models import User, Recipe, Association, Ingre, Recipe_ingre




user=User.query.filter_by(username="xiaofan").first()
recipe=Recipe.query.filter_by(recipename="Jerry").first()
recipes = Recipe.query.filter(Recipe.users.any(username="xiaofan")).all()

if recipe not in recipes:
    user.add_recipes([recipe])

    # commit the changes
    db.session.commit()
