from actual import ActualNode

class FileNode(ActualNode):

  def __str__(self):
    return '%s %s: %s' % (self.parent, self.path, self.__rest)
