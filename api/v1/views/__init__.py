#!/usr/bin/python3
"""
API v1 views initializer
"""
from flask import Blueprint

from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import*
from api.v1.views.users import *
from api.v1.views.places_reviews import *

app_views = Blueprint('airbnb', __name__, url_prefix='/api/v1')

# This imports the new views here
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.amenities import *
from api.v1.views.places import get_places, get_place, delete_place, create_place, update_place
from api.v1.views.places_amenities import *
