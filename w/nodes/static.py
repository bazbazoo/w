from file import FileNode

class StaticNode(FileNode):
  def __str__(self):
    return FileNode.__str__(self) + " (static)"

  def _GET(self):
    return str(self)
