#!/usr/bin/python3
"""
Contains the blueprint for the API.

This module is responsible for initializing the Flask blueprint by,
defining the URL prefix and importing all view modules for the API endpoints
"""

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


from api.v1.views.amenities import *
from api.v1.views.cities import *
from api.v1.views.index import *
from api.v1.views.places_amenities import *
from api.v1.views.places import *
from api.v1.views.places_reviews import *
from api.v1.views.states import *
from api.v1.views.users import *
