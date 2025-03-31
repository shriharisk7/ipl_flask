from flask import Blueprint, render_template, request
# from src.models import User

router = Blueprint('router', __name__)

@router.route('/')
def index():
    return "DBOSS"