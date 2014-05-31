from web import forbidden

from node import Node

def forbidden_response(why = "nope"):
  forbidden()
  return "forbidden: %s" % why

class ForbiddenNode(Node):
  def __call__(self, method):
    forbidden_response()

  def resolve(self, path):
    return self