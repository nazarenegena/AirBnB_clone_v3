#!/usr/bin/python3

from flask import Blueprint


app_views = Blueprint('airbnb', __name__, url_prefix='/api/v1')
