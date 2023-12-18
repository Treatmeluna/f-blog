from flask import Blueprint

main = Blueprint('main', __name__)

from .import views, forms
from ..models import Permission

# template 에서 Permission 을 확인하기 위해
@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)