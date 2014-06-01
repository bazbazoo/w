from actual import ActualNode

class FileNode(ActualNode):

  def __str__(self):
    return '%s %s: %s' % (self.parent, self.path, self.__rest)

  def _DELETE(self):
    raise NotImplementedError

  def _PUT(self):
    raise NotImplementedError
