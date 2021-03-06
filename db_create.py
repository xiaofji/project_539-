from project import db
from project.models import User, Recipe, Association, Ingre, Recipe_ingre


# create the database and the db table
db.create_all()
# insert data

ingre1 = Ingre(ingrename="chili", url="../static/img/Chili.jpg")
ingre2 = Ingre(ingrename="chicken", url="../static/img/Chicken.jpg")
ingre3 = Ingre(ingrename="shrimp ball", url="../static/img/ShrimpBall.jpg")
ingre4 = Ingre(ingrename="fish slice", url="../static/img/FishSlice.jpg")
ingre5 = Ingre(ingrename="water", url="../static/img/Water.jpg")
ingre6 = Ingre(ingrename="soy sauce", url="../static/img/SoySauce.jpg")
ingre7 = Ingre(ingrename="green onion", url="../static/img/GreenOnions.jpg")
ingre8 = Ingre(ingrename="bitter melon", url="../static/img/BitterMelon.jpg")
ingre9 = Ingre(ingrename="mayonnaise", url="../static/img/Mayonnaise.jpg")
ingre10 = Ingre(ingrename="prickly ash", url="../static/img/PricklyAsh.jpg")
ingre11 = Ingre(ingrename="thick bean sauce", url="../static/img/ThickBeanSauce.jpg")

db.session.add_all([ingre1, ingre2, ingre3, ingre4, ingre5, ingre6, ingre7, ingre8, ingre9, ingre10, ingre11])

instruct1 = "Hello! Welcome to my kitchen.|Today I am going to teach you how to cook the sliced cold chicken.|Cut a chicken to small pieces|add|add|Boil the chicken for 10 mins|Poul out all the water|add|Cut the greenonions|add|Congratuations! You have finished learning this dish!"
instruct2 = "Hello! Welcome to my kitchen.|Today I am going to teach you how to cook the Sichuan fish.|add|add|add|Fry 5min|add|Boil for 10mins.|add|Boil for 6mins|Congratuations! You have finished learning this dish!"
instruct3 = "Hello! Welcome to my kitchen.|Today I am going to teach you how to cook the bitter shrimp ball.|Slice the bitter melon and put it at the bottom.|add|add|add|Steam for 20mins|add|Congratuations! You have finished learning this dish!"

recipe1 = Recipe(id=1,recipename="sliced_cold_chicken", ingresorder="2 5 6 7", instruction = instruct1)
recipe2 = Recipe(id=2,recipename="sichuan_fish", ingresorder="11 10 1 5 4", instruction = instruct2)
recipe3 = Recipe(id=3,recipename="bitter_shrimp_ball", ingresorder="8 3 9 7", instruction = instruct3)
recipe4 = Recipe(id=4,recipename="crystal_shrimp", ingresorder="1", instruction = " ")
recipe5 = Recipe(id=5,recipename="buddha_Jumps_over_the_wall", ingresorder="1", instruction = " ")
recipe6 = Recipe(id=6,recipename="steamed_preserved_hams", ingresorder="1", instruction = " ")
recipe7 = Recipe(id=7,recipename="phoenix_peony_stew", ingresorder="1", instruction = " ")
recipe8 = Recipe(id=8,recipename="jellyfish_with_vinegar", ingresorder="1", instruction = " ")



recipe1.add_ingres([ingre2, ingre5, ingre6, ingre7])
recipe2.add_ingres([ingre4, ingre1, ingre5, ingre11, ingre10])
recipe3.add_ingres([ingre8, ingre3, ingre9, ingre7])


user1 = User( username = "admin", password = "admin")
user2 = User( username = "siyu", password = "siyu")


user1.add_recipes([ recipe1 , recipe3, recipe2, recipe4, recipe5, recipe6, recipe7, recipe8 ])
user2.add_recipes([ recipe2 , recipe1 ])

# commit the changes
db.session.commit()
