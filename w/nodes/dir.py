from os import listdir
from os.path import isdir
from shutil import rmtree

from ..utils import S, J
from actual import ActualNode
from config import CONFIG_DIR_NAME
from forbidden import ForbiddenNode, forbidden_response

FORBIDDEN_NAMES = ['.', '..', CONFIG_DIR_NAME]

class DirNode(ActualNode):

  def _GET(self):
    files = filter(lambda d: d not in FORBIDDEN_NAMES, listdir(self.path))
    decorate = lambda n: "%s%s" % (n, isdir(J(self.path, n)) and '/' or '')
    return '\n'.join(map(decorate, files))

  def _DELETE(self):
    if self.parent is None:
      return forbidden_response("can not delete root directory")
    else:
      rmtree(self.path)

  def _PUT(self):
    return forbidden_response("PUT on directory not supported")

  def _POST(self):
    return forbidden_response("POST on directory not supported")

  def resolve(self, path):
    from factory import node # break circular dependency.

    if path is None: return self

    head, rest = S(path)

    if head == '': return self.resolve(rest)

    next_path = J(self.path, head)
    if head in FORBIDDEN_NAMES:
      return ForbiddenNode(next_path, self)

    next_node = node(next_path, self)
    return next_node.resolve(rest)
