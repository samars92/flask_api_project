from flask import Blueprint, session,abort

index = Blueprint('index',__name__)
@index.route('/')
def hello():
    return "Hello World from app 1!"