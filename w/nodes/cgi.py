from file import FileNode

class CGINode(FileNode):
  def __str__(self):
    return FileNode.__str__(self) + " (cgi)"

  def _GET(self):
    return str(self)

