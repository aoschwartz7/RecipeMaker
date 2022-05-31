from flask import Blueprint

from flask_restful import reqparse, Resource, marshal_with, fields
from recipe_api.recipeModel import Recipes


recipe_put_args = reqparse.RequestParser(bundle_errors=True)
recipe_put_args.add_argument(
    "name", type=str, help="Name of recipe is required", required=True, location="form"
)
recipe_put_args.add_argument(
    "ingredients",
    type=str,
    action="append",
    help="Ingredients list is required",
    required=True,
    location="form",
)
recipe_put_args.add_argument(
    "instructions",
    type=str,
    action="append",
    help="Instructions list is required",
    required=True,
    location="form",
)


class RecipeNamesList(Resource):
    # prepare return data to be serialized with marshal
    mfields = {"recipeNames": fields.List(fields.String)}

    @marshal_with(mfields)
    def get(self) -> list[str]:
        recipes = [recipe.get("name") for recipe in Recipes.load()]
        return {"recipeNames": recipes}, 200


class GetRecipeName(Resource):
    mfields = {
        "details": fields.Nested(
            {"ingredients": fields.List(fields.String), "numSteps": fields.Integer}
        )
    }

    @marshal_with(mfields)
    def get(self, recipe_name: str):
        response = {}
        recipes: list = Recipes.load()
        recipe = Recipes.get_by_name(recipes, recipe_name)

        if recipe:
            response = {
                "details": {
                    "ingredients": recipe.get("ingredients"),
                    "numSteps": len(recipe.get("instructions")),
                }
            }

        return response, 200


class AddRecipe(Resource):
    # TODO: marshal_with
    def post(self):
        data = recipe_put_args.parse_args()
        recipes = Recipes.load()
        existing_recipe = Recipes.get_by_name(recipes, data.get("name"))

        if existing_recipe:
            return {"error": "Recipe already exists"}, 400

        recipes.append(data)
        Recipes.write(recipes)
        return "", 201


class updateRecipe(Resource):
    # TODO: marshal_with
    def put(self):
        data = recipe_put_args.parse_args()
        recipes = Recipes.load()
        existing_recipe = Recipes.get_by_name(recipes, data.get("name"))

        if not existing_recipe:
            return {"error": "Recipe does not exist"}, 404

        Recipes.update_recipe(existing_recipe, data)
        Recipes.write(recipes)
        return "", 204


bp = Blueprint("auth", __name__, url_prefix="/auth")
