from project import db
from project.models import User, Recipe, Association, Ingre, Recipe_ingre


# create the database and the db table
db.create_all()
# insert data

ingre1 = Ingre(ingrename="chili", url="static/img/Chili.jpg")
ingre2 = Ingre(ingrename="chicken", url="static/img/Chicken.jpg")
ingre3 = Ingre(ingrename="shrimp ball", url="static/img/ShrimpBall.jpg")
ingre4 = Ingre(ingrename="fish slice", url="static/img/FishSlice.jpg")
ingre5 = Ingre(ingrename="water", url="static/img/Water.jpg")
ingre6 = Ingre(ingrename="soy sauce", url="static/img/SoySauce.jpg")
ingre7 = Ingre(ingrename="green onion", url="static/img/GreenOnions.jpg")
ingre8 = Ingre(ingrename="bitter melon", url="static/img/BitterMelon.jpg")
ingre9 = Ingre(ingrename="mayonnaise", url="static/img/Mayonnaise.jpg")
ingre10 = Ingre(ingrename="prickly ash", url="static/img/PricklyAsh.jpg")
ingre11 = Ingre(ingrename="thick bean sauce", url="static/img/ThickBeanSauce.jpg")

db.session.add_all([ingre1, ingre2, ingre3, ingre4, ingre5, ingre6, ingre7, ingre8, ingre9, ingre10, ingre11])

recipe1 = Recipe(id=1,recipename="sliced_cold_chicken", ingresorder="2 5 6 7")
recipe2 = Recipe(id=2,recipename="sichuan_fish", ingresorder="11 10 1 5 4")
recipe3 = Recipe(id=3,recipename="bitter_shrimp_ball", ingresorder="8 3 9 7")
recipe1.add_ingres([ingre2, ingre5, ingre6, ingre7])
recipe2.add_ingres([ingre4, ingre1, ingre5, ingre11, ingre10])
recipe3.add_ingres([ingre8, ingre3, ingre9, ingre7])


user1 = User( username = "admin", password = "admin")
user2 = User( username = "siyu", password = "siyu")


user1.add_recipes([ recipe1 , recipe3 ])
user2.add_recipes([ recipe2 , recipe1 ])

# commit the changes
db.session.commit()
