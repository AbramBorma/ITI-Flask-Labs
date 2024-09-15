from flask import Blueprint

auth = Blueprint(
    "auth",
    __name__,
    url_prefix="", 
    static_folder='static',
    template_folder='templates'
)

from . import views
