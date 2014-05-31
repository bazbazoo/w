from web import forbidden

from node import Node

class __ForbiddenNode(Node):
  def __init__(self, path, logger):
    Node.__init__(self, path, logger)

  def __call__(self, method):
    forbidden()
    return "forbidden"

def forbidden_node(path, logger):
  return __ForbiddenNode(path, logger)

def to_forbidden_node(node, logger):
  return forbidden_node(node.path, logger)