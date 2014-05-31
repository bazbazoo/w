from actual import ActualNode

class FileNode(ActualNode):
  def __init__(self, path, parent, rest = None):
    ActualNode.__init__(self, path, parent)
    self.__rest = rest
    self.__parent = parent

  def __str__(self):
    return '%s %s: %s' % (self.parent, self.path, self.__rest)

  def resolve(self, path):
    assert self.__rest is None
    return self.__class__(self.path, self.parent, path)
