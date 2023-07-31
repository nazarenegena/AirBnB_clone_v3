#!/usr/bin/python3

# airbnb api
import os
from models import storage
from flask import Flask
from api.v1.views import app_views
from flask_cors import CORS

app = Flask(__name__)

# Register the app_views blueprint
app.register_blueprint(app_views)

#CORS instance allowing for 0.0.0.0
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})

# Teardown function to close the storage when the app context tears down
@app.teardown_appcontext
def close_storage(exception=None):
    storage.close()

# Not found url
@app.errorhandler(404)
def not_found(error):
    response = {
        "error": "Not found"
    }
    return jsonify(response), 404

if __name__ == '__main__':
    # Set the host and port from environment variables or use default values
    host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
    port = int(os.environ.get('HBNB_API_PORT', 5000))
     
    app.run(host=host, port=port, threaded=True)
