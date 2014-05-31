from ..utils import S, J

from actual import ActualNode
from forbidden import ForbiddenNode

class DirNode(ActualNode):

  def _GET(self):
    return str(self)

  def __str__(self):
    return self.path

  def resolve(self, path):
    from factory import node # break circular dependency.

    if path is None: return self

    head, rest = S(path)

    if head == '': return self.resolve(rest)

    next_path = J(self.path, head)
    if head == '..': return ForbiddenNode(next_path, self)

    next_node = node(next_path, self)
    return next_node.resolve(rest)
