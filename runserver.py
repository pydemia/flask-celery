"""Main entrypint of the application."""
# Api factory import
from api import factory

# Eventually force the environment
# factory.environment = 'default'

# Get flask instance
flask_app = factory.flask_app

# Get celery instance
celery_app = factory.celery_app

if __name__ == '__main__':
    # Actually run the application
    flask_app.run(debug=True, host='0.0.0.0', port=80)
