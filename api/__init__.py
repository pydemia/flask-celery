"""

api/
    __init__.py
    app.py          # this file contains your app and routes
    resources/
        __init__.py
        foo.py      # contains logic for /Foo
        bar.py      # contains logic for /Bar
    common/
        __init__.py
        utils.py     # just some common infrastructure
"""


"""Initialization module of the package.
<https://github.com/matthieugouel/python-flask-celery-example/blob/master/api/__init__.py>
"""
# API Factory imports
from api.factory import Factory

# API configuration imports
from api.config import Config

# Version handling
import pkg_resources

try:
    # If the app is packaged
    # Get the version of the setup package
    __version__ = pkg_resources.get_distribution('api').version
except pkg_resources.DistributionNotFound:  # pragma: no cover
    # If app is not used as a package
    # Hardcode the version from the configuration file
    __version__ = Config.VERSION


# Instantiation of the factory
factory = Factory()

# Enable flask instance
factory.run_flask()

# Enable of the desired plugins
factory.run_celery()


# API Resources imports
from api.resources import api_blueprint  # noqa: E402

# Register the blueprint
factory.register_flask_blueprint(api_blueprint)
