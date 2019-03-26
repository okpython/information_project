from flask import Blueprint

index_bule = Blueprint("index", __name__)

from . import views