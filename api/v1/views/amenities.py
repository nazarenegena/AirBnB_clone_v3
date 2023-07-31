#!/usr/bin/python3
"""
Amenities API views
"""

from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage, Amenity


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def get_amenities():
    """
    Retrieves the list of all Amenity objects
    """
    amenities = storage.all(Amenity).values()
    return jsonify([amenity.to_dict() for amenity in amenities])


@app_views.route('/amenities/<amenity_id>', methods=['GET'], strict_slashes=False)
def get_amenity(amenity_id):
    """
    Retrieves a Amenity object by its id
    """
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'], strict_slashes=False)
def delete_amenity(amenity_id):
    """
    Deletes a Amenity object by its id
    """
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    storage.delete(amenity)
    storage.save()
    return jsonify({}), 200


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def create_amenity():
    """
    Creates a new Amenity object
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    if 'name' not in data:
        return jsonify({"error": "Missing name"}), 400
    new_amenity = Amenity(**data)
    new_amenity.save()
    return jsonify(new_amenity.to_dict()), 201


@app_views.route('/amenities/<amenity_id>', methods=['PUT'], strict_slashes=False)
def update_amenity(amenity_id):
    """
    Updates a Amenity object
    """
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)

    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400

    # Ignore keys: id, created_at, and updated_at
    ignored_keys = ['id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in ignored_keys:
            setattr(amenity, key, value)

    storage.save()
    return jsonify(amenity.to_dict()), 200

