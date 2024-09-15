from flask import Blueprint

book = Blueprint(
    "book",
    __name__,
    url_prefix="", 
    static_folder='static',
    template_folder='templates'
)

from . import views
