from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
from recipe import Recipe, get_recipe_book

recipeBook = get_recipe_book()
# automatically parse through requests that are sent and make sure it matches guidelines
recipe_put_args = reqparse.RequestParser()
# list mandatory arguments
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

# recipeBookJSON = json.dumps(recipeBook)


app = Flask(__name__)
api = Api(app)  # wrap app in a restful API

# TODO: Can combine classes with same path


class AllRecipeNames(Resource):
    def get(self):
        return {"recipeNames": [n.name for n in recipeBook]}, 200


class GetRecipeName(Resource):
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
            return {"recipe": args}, 201


class updateRecipe(Resource):
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


api.add_resource(AllRecipeNames, "/recipes")
api.add_resource(GetRecipeName, "/recipes/details/<string:recipe_name>")
api.add_resource(AddRecipe, "/recipes")
api.add_resource(updateRecipe, "/recipes")
