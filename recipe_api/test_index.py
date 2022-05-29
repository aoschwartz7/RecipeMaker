import unittest
import index
import requests


# class TestFlaskApiUsingRequests(unittest.TestCase):
#     def test_hello_world(self):
#         response = requests.get("http://localhost:5000/recipes")
#         print(response)
#         self.assertEqual(response.json(), {"hello": "world"})


class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = index.app.test_client()

    def test_hello_world(self):
        response = self.app.get("/recipes")
        print(response)


if __name__ == "__main__":
    unittest.main()
