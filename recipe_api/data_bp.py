import functools

from flask import Blueprint

from flask_restful import reqparse, Resource, marshal_with, fields
from recipeModel import Recipe, get_recipe_book

recipeBook = get_recipe_book("data.json")

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
        return {"recipeNames": [n.name for n in recipeBook]}, 200


class GetRecipeName(Resource):
    mfields = {
        "details": fields.Nested(
            {"ingredients": fields.List(fields.String), "numSteps": fields.Integer}
        )
    }

    @marshal_with(mfields)
    def get(self, recipe_name: str):
        names = [r.name for r in recipeBook]
        if recipe_name in names:
            recipe = next((r for r in recipeBook if r.name == recipe_name), None)
            return {
                "details": {
                    "ingredients": recipe.ingredients,
                    "numSteps": recipe.numSteps,
                }
            }, 200

        else:
            return {}, 200


class AddRecipe(Resource):
    # TODO: marshal_with
    def post(self):
        args = recipe_put_args.parse_args()
        if args.name in [r.name for r in recipeBook]:
            return {"error": "Recipe already exists"}, 400
        else:
            recipeBook.append(
                Recipe(
                    args.name,
                    args.ingredients,
                    args.instructions,
                    len(args.instructions),
                )
            )
            return {}, 201


class updateRecipe(Resource):
    # TODO: marshal_with
    def put(self):
        args = recipe_put_args.parse_args()
        if args.name in [r.name for r in recipeBook]:
            for i, o in enumerate(recipeBook):
                if o.name == args.name:
                    del recipeBook[i]
                    recipeBook.append(
                        Recipe(
                            args.name,
                            args.ingredients,
                            args.instructions,
                            len(args.instructions),
                        )
                    )
            return {}, 201
        else:
            return {"error": "Recipe does not exist"}, 404


bp = Blueprint("auth", __name__, url_prefix="/auth")
