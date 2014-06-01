from node import Node

class CGINode(Node):
  def __init__(self, path, parent, rest = None):
    Node.__init__(path, parent)
    self.__rest = rest

  def resolve(self, path):
    assert self.__rest is None
    return self.__class__(self.path, self.parent, rest = path)

  def __call__(self, method):
    raise NotImplementedError
