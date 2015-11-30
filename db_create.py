from project import db
from project.models import User, Recipe, Association, Ingre, Recipe_ingre


# create the database and the db table
db.create_all()
# insert data

ingre1 = Ingre(ingrename="chili", url="static/img/")
ingre2 = Ingre(ingrename="chicken", url="static/img/")
ingre3 = Ingre(ingrename="shrimp", url="static/img/")
ingre4 = Ingre(ingrename="fish", url="static/img/")

db.session.add_all([ingre1, ingre2, ingre3, ingre4])

recipe1 = Recipe(id=1,recipename="sliced cold chicken", ingresorder="2")
recipe2 = Recipe(id=2,recipename="sichuan fish", ingresorder="4 1")
recipe3 = Recipe(id=3,recipename="crystal shrimp", ingresorder="1 3")
recipe1.add_ingres([ingre2])
recipe2.add_ingres([ingre4, ingre1])
recipe3.add_ingres([ingre3, ingre1])


user1 = User( username = "admin", password = "admin")
user2 = User( username = "siyu", password = "siyu")


user1.add_recipes([ recipe1 , recipe3 ])
user2.add_recipes([ recipe2 , recipe1 ])

# commit the changes
db.session.commit()
