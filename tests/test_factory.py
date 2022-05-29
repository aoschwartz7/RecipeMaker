from recipe_api import create_app


def test_config():
    assert not create_app().testing
    assert create_app({"TESTING": True}).testing


def test_recipes(client):
    response = client.get("/recipes")
    assert response.data == b"{'recipeNames': ['scrambledEggs', 'garlicPasta', 'chai']}"
