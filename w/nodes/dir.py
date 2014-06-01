from os import listdir
from os.path import isdir
from shutil import rmtree

from ..utils import S, J
from actual import ActualNode
from forbidden import ForbiddenNode, forbidden_response

class DirNode(ActualNode):

  def _GET(self):
    decorate = lambda n: "%s%s" % (n, isdir(J(self.path, n)) and '/' or '')
    return '\n'.join(map(decorate, listdir(self.path)))

  def _DELETE(self):
    if self.parent is None:
      return forbidden_response("can not delete root directory")
    else:
      rmtree(self.path)

  def _PUT(self):
    return forbidden_response("PUT on directory not supported")

  def _POST(self):
    return forbidden_response("POST on directory not supported")

  def __str__(self):
    return self.path

  def resolve(self, path):
    from factory import node # break circular dependency.

    if path is None: return self

    head, rest = S(path)

    if head in ['', '.']: return self.resolve(rest)

    next_path = J(self.path, head)
    if head == '..': return ForbiddenNode(next_path, self)

    next_node = node(next_path, self)
    return next_node.resolve(rest)
