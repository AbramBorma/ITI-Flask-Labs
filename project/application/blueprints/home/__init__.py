from flask import Blueprint

home = Blueprint(
    "home",
    __name__,
    url_prefix="", 
    static_folder='static',
    template_folder='templates'
)

from . import views
