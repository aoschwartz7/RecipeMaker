from flask import Flask, Blueprint
from flask_restful import Api
from data_bp import (
    RecipeNamesList,
    GetRecipeName,
    AddRecipe,
    updateRecipe,
)

app = Flask(__name__)
api_bp = Blueprint("api", __name__)
app.config.from_object("config.DevConfig")
api = Api(app)  # wrap app in a restful API


api.add_resource(RecipeNamesList, "/recipes")
api.add_resource(GetRecipeName, "/recipes/details/<string:recipe_name>")
api.add_resource(AddRecipe, "/recipes")
api.add_resource(updateRecipe, "/recipes")

app.register_blueprint(api_bp)


if __name__ == "__main__":
    app.run(debug=True)
