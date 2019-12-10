from flask import Blueprint, request
from .dao import dao

api = Blueprint('api', __name__, template_folder='templates')

@api.route('/post', methods=['GET'])
def get_post():
  body = request.get_json()
  if body is None:
    body = {}
    body['username'] = request.args.get('username')
    body['index'] = int(request.args.get('index','0'))
  print(f"/api/post {body}")
  post = dao.get_post(body.get('username'), body.get('index'))
  if post is None:
    return "Nothing", 404
  return post