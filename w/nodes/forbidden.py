from web import forbidden

from node import Node

class ForbiddenNode(Node):
  def __call__(self, method):
    forbidden()
    return "forbidden"

  def resolve(self, path):
    return self