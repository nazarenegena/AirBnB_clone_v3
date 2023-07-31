#!/usr/bin/python3

from api.v1.views import app_views
from flask import jsonify
from models import storage

@app_views.route("/status", methods=["GET"], strict_slashes=False)
def status():
    response = {
        "status": "OK"
    }
    return jsonify(response)

@app_views.route("/api/v1/stats", methods=["GET"], strict_slashes=False)
def get_stats():
    """Retrieve the number of each object by type"""
    obj_counts = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User')
    }
    return jsonify(obj_counts)
