from actual import ActualNode

class FileNode(ActualNode):

  def __str__(self):
    return '%s %s: %s' % (self.parent, self.path, self.__rest)

  def _GET(self):
    raise NotImplementedError

  def _DELETE(self):
    remove(self.path)

  def _PUT(self):
    with open(self.path, 'wb') as f:
      f.write(data())

  def _POST(self):
    return forbidden_response("already exists")
