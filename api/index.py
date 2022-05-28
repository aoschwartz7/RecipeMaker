from flask import Flask
from flask_restful import Api
from api.resources.resources import (
    RecipeNamesList,
    GetRecipeName,
    AddRecipe,
    updateRecipe,
)

app = Flask(__name__)
api = Api(app)  # wrap app in a restful API
app.config.from_object("config.DevConfig")


api.add_resource(RecipeNamesList, "/recipes")
api.add_resource(GetRecipeName, "/recipes/details/<string:recipe_name>")
api.add_resource(AddRecipe, "/recipes")
api.add_resource(updateRecipe, "/recipes")
