from project import db, bcrypt


class Association(db.Model):
    __tablename__ = 'association'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), primary_key=True)
    user = db.relationship("User", backref=db.backref("association", cascade="all, delete-orphan" ))
    recipe = db.relationship("Recipe", backref=db.backref("association", cascade="all, delete-orphan" ))

    def __init__(self, user=None, recipe=None):
        self.user = user
        self.recipe =  recipe

class Recipe_ingre(db.Model):
    __tablename__ = 'recipe_ingre'
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), primary_key=True)
    ingre_id = db.Column(db.Integer, db.ForeignKey('ingres.id'), primary_key=True)
    recipe = db.relationship("Recipe", backref=db.backref("recipe_ingre", cascade="all, delete-orphan" ))
    ingre = db.relationship("Ingre", backref=db.backref("recipe_ingre", cascade="all, delete-orphan" ))

    def __init__(self, recipe=None, ingre=None):
        self.recipe = recipe
        self.ingre =  ingre

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    recipes = db.relationship("Recipe", secondary="association", viewonly=True)


    def __init__(self, username, password):
        self.username = username
        # self.password = password
        self.password = bcrypt.generate_password_hash(password)


    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<username> {}'.format(self.username)

    def add_recipes(self, recipes):
        for recipe in recipes:
            self.association.append(Association(user=self, recipe=recipe))

class Recipe(db.Model):

    __tablename__ = "recipes"

    id = db.Column(db.Integer, primary_key=True)
    recipename = db.Column(db.String, nullable=False)
    users = db.relationship("User", secondary="association", viewonly=True)


    def __init__(self, id, recipename):
        self.id = id
        self.recipename = recipename

    def __repr__(self):
        return '<recipename> {}'.format(self.recipename)

    def add_ingres(self, ingres):
        for ingre in ingres:
            self.recipe_ingre.append(Recipe_ingre(recipe=self, ingre=ingre))

class Ingre(db.Model):

    __tablename__ = "ingres"

    id = db.Column(db.Integer, primary_key=True)
    ingrename = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
    recipes = db.relationship("Recipe", secondary="recipe_ingre", viewonly=True)


    def __init__(self, ingrename, url):
        # self.id = id
        self.ingrename = ingrename
        self.url = url

    def __repr__(self):
        return '<ingrename> {}'.format(self.ingrename)
