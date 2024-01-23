from flask import Blueprint, request

test = Blueprint('test', __name__)

@test.post('/')
def post_test():
    return "test"
