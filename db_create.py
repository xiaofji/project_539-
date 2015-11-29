from project import db
from project.models import User, Recipe, Association, Ingre, Recipe_ingre


# create the database and the db table
db.create_all()
# insert data

ingre1 = Ingre(ingrename="rice", url="static/img/")
ingre2 = Ingre(ingrename="chicken", url="static/img/")
ingre3 = Ingre(ingrename="beef", url="static/img/")

db.session.add_all([ingre1, ingre2, ingre3])

recipe1 = Recipe(id=1,recipename="Tom")
recipe2 = Recipe(id=2,recipename="Jerry")
recipe3 = Recipe(id=3,recipename="Marie")
recipe1.add_ingres([ingre1, ingre2])
recipe2.add_ingres([ingre2])
recipe3.add_ingres([ingre3, ingre1])


user1 = User( username = "admin", password = "admin")
user2 = User( username = "siyu", password = "siyu")


user1.add_recipes([ recipe1 , recipe3 ])
user2.add_recipes([ recipe2 , recipe1 ])

# commit the changes
db.session.commit()
