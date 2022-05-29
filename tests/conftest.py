import os
import tempfile

import pytest
from recipe_api import create_app


@pytest.fixture
def app():

    temp_file, temp_file_path = tempfile.mkstemp()

    app = create_app({"TESTING": True})

    with app.app_context():
        # init_db()
        # get_db().executescript(_data_sql)
        print("HELLLLLLO")

    # yield app

    # os.close(db_fd)
    # os.unlink(db_path)


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
