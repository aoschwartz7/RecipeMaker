import unittest
from unittest.mock import Mock
from unittest.mock import patch
import requests


class RecipeApiTest(unittest.TestCase):
    BASE = "http://127.0.0.1:5000/"
    RECIPES_URL = f"{BASE}/recipes"

    ALL_RECIPES = {"recipeNames": ["scrambledEggs", "garlicPasta", "chai"]}
    RECIPE_DETAILS = {
        "details": {
            "ingredients": [
                "500mL water",
                "100g spaghetti",
                "25mL olive oil",
                "4 cloves garlic",
                "Salt",
            ],
            "numSteps": 5,
        }
    }

    NEW_RECIPE = {
        "name": "butteredBagel",
        "ingredients": ["1 bagel", "butter"],
        "instructions": ["cut the bagel", "spread butter on bagel"],
    }
    UPDATE_RECIPE = {
        "name": "butteredBagel",
        "ingredients": ["1 bagel", "2 tbsp butter"],
        "instructions": ["cut the bagel", "spread butter on bagel"],
    }

    UPDATE_RECIPE_NOT_IN_BOOK = {
        "name": "pecanPie",
        "ingredients": ["1 pie crust", "12 tbsp butter", "other"],
        "instructions": ["thaw crust", "etc"],
    }

    def test_1_get_all_recipes(self):
        r = requests.get(RecipeApiTest.RECIPES_URL)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.headers["Content-Type"], "application/json")

    def test_2_get_recipe_details(self):
        recipe = "/details/garlicPasta"
        r = requests.get(RecipeApiTest.RECIPES_URL + recipe)
        self.assertEqual(r.status_code, 200)

    def test_3_add_recipe(self):
        try:  # see if recipe already exists
            r = requests.get(RecipeApiTest.RECIPES_URL, data=RecipeApiTest.NEW_RECIPE)
        except:
            r = requests.post(RecipeApiTest.RECIPES_URL, data=RecipeApiTest.NEW_RECIPE)
            self.assertEqual(r.status_code, 400)

    def test_5_update_recipe(self):
        r = requests.put(RecipeApiTest.RECIPES_URL, data=RecipeApiTest.UPDATE_RECIPE)

    def test_6_update_recipe_not_in_book(self):
        r = requests.put(
            RecipeApiTest.RECIPES_URL,
            data=RecipeApiTest.UPDATE_RECIPE_NOT_IN_BOOK,
        )
        self.assertEqual(r.status_code, 404)
        self.assertEqual(r.json(), {"error": "Recipe does not exist"})


if __name__ == "__main__":
    unittest.main()
