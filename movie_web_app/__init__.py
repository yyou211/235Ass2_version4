"""Initialize Flask app."""
import os

from flask import Flask

import movie_web_app.adapters.repository as repo
from movie_web_app.adapters.memory_repository import MemoryRepository, populate

def create_app(test_config = None):

    app = Flask(__name__)
    app.config.from_object('config.Config')
    data_path = "/Users/vivian/Desktop/235Ass2_version4/movie_web_app/adapters/data"

    if test_config is not None:
        # Load test configuration, and override any configuration settings.
        app.config.from_mapping(test_config)
        data_path = app.config['TEST_DATA_PATH']

    repo.repo_instance = MemoryRepository()
    populate(data_path, repo.repo_instance)

    with app.app_context():
        from .home import home
        app.register_blueprint(home.home_blueprint)

        from .movie import movie
        app.register_blueprint(movie.movie_blueprint)

        from .authentication import authentication
        app.register_blueprint(authentication.authentication_blueprint)

        from .utilities import utilities
        app.register_blueprint(utilities.utilities_blueprint)

    return app


