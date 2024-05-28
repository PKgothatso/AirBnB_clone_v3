#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint
from api.v1.views.index import
from api.v1.views.states import
from api.v1.views.places import
from api.v1.views.places_reviews import
from api.v1.views.cities import handle_cities, get_cities
from api.v1.views.amenities import AmenityView, handle_amenities,
from api.v1.views.users import UsersView
from api.v1.views.places_amenities import Places_AmentiesView,
handle_places_amenities, get_place_amenities

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
