from web import internalerror

from ..utils import wexecute
from common import protected
from node import Node

class CGINode(Node):
  def __init__(self, path, parent, rest = None):
    Node.__init__(self, path, parent)
    self.__rest = rest

  def resolve(self, path):
    assert self.__rest is None
    return self.__class__(self.path, self.parent, rest=path)

  @protected
  def __call__(self, method):
    rc, out, err = wexecute(self.path, { 'REMAINING_PATH': self.__rest or '' })

    if err: print err # TODO: log

    if rc != 0:
      raise internalerror()
    else:
      return out
