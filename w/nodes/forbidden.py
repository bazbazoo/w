from web import forbidden

from node import Node

def forbidden_response():
  forbidden()
  return "forbidden"

class ForbiddenNode(Node):
  def __call__(self, method):
    forbidden_response()

  def resolve(self, path):
    return self