from file import FileNode

class CGINode(FileNode):
  def __init__(self, path, parent, rest = None):
    FileNode.__init__(path, parent)
    self.__rest = rest

  def __str__(self):
    return FileNode.__str__(self) + " (cgi)"

  def _GET(self):
    return str(self)

  def resolve(self, path):
    assert self.__rest is None
    return self.__class__(self.path, self.parent, rest = path)
