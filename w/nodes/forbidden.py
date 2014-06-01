from web import forbidden

from node import Node

def forbidden_response(why = "nope"):
  forbidden()
  return "forbidden: %s" % why

class ForbiddenNode(Node):
  def __init__(self, path, parent, msg = ''):
    Node.__init__(self, path, parent)
    self.__msg = msg

  def __call__(self, method):
    return forbidden_response(self.__msg)

  def resolve(self, path):
    return self