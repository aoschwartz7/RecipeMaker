import requests
import json

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "recipes")

response = requests.post(
    BASE + "recipes",
    {
        "name": "pie",
        "ingredients": ["Frozen pie", "whipped cream"],
        "instructions": [
            "Go to store and buy pie",
            "Put in oven",
            "Cool and add whipped cream",
        ],
    },
)

# response = requests.put(
#     BASE + "recipes",
#     {
#         "name": "garlicPasta",
#         "ingredients": ["Frozen pie", "whipped cream"],
#         "instructions": [
#             "Go to store and buy pie",
#             "Put in oven",
#             "Cool and add whipped cream",
#         ],
#     },
# )


print(response.json())
