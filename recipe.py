from marshmallow import Schema, fields, post_load
from typing import Union
import json


class Recipe:
    # all_recipes = []

    def __init__(
        self,
        name: str,
        ingredients: Union[str, list[str]],
        instructions: Union[str, list[str]],
        numSteps: int,
    ) -> None:
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.numSteps = len(instructions)
        # self.type = type
        # Recipe.all_recipes.append(name)

    def __repr__(self):
        return f"""<Recipe(
                name={self.name}, 
                ingredients={self.ingredients}, 
                instructions={self.instructions},
                numSteps={self.numSteps}
                )>"""


# Used to deserialize and serialize instances of Recipe
class RecipeSchema(Schema):
    name = fields.Str()
    ingredients = fields.List(fields.Str())
    instructions = fields.List(fields.Str())
    numSteps = fields.Int()


class RecipeUploadSchema(RecipeSchema):
    @post_load
    def make_recipe(self, data):
        return Recipe(**data)


# Create recipe book from recipes data
def get_recipe_book() -> list[object]:
    with open("data.json") as f:
        recipesJSON = json.load(f)
        recipeBook = []
        for r in recipesJSON["recipes"]:
            recipe = Recipe(
                name=r["name"],
                ingredients=r["ingredients"],
                instructions=r["instructions"],
                numSteps=len(r["instructions"]),
            )
            recipeBook.append(recipe)
    return recipeBook
