from os.path import isdir, isfile

from actual import ActualNode
from file import FileNode
from missing import MissingNode
from forbidden import ForbiddenNode

from ..utils import S, J

class DirNode(ActualNode):
  def _GET(self):
    return str(self)

  def __str__(self):
    return self.path

  def __node(path):
    if isdir(path):
      node_type = DirNode
    elif isfile(path):
      node_type = FileNode
    else:
      node_type = MissingNode
    return node_type(path, self)

  def resolve(self, path):
    if path is None: return self

    head, rest = S(path)

    if head == '': return self.resolve(rest)

    next_path = J(self.path, head)
    if head == '..': return ForbiddenNode(next_path, self)

    next_node = __node(next_path)
    return next_node.resolve(rest)
