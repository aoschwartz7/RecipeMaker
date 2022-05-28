from typing import Union
import json
from pathlib import Path


class Recipe:
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

    def __repr__(self):
        return f"""<Recipe(
                name={self.name}, 
                ingredients={self.ingredients}, 
                instructions={self.instructions},
                numSteps={self.numSteps}
                )>"""


# Create recipe book from recipes data
def get_recipe_book(jsonDataFile: str) -> list[object]:
    jsonDataFile = Path(jsonDataFile)
    assert (
        jsonDataFile.exists()
    ), f"No such data file containing recipes: {jsonDataFile}"
    with open(jsonDataFile) as f:
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
