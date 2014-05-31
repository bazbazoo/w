from os.path import isfile

from ..utils import J

from actual import ActualNode

class __FileNode(ActualNode):
  def __init__(self, path, parent, after, logger):
    ActualNode.__init__(self, path, logger)
    self.__after = after
    self.__parent = parent

  def _GET(self):
    return str(self)

  def __str__(self):
    return '%s %s: %s' % (self.__parent, self.path, self.__after)

def file_node(path, parent, afters, logger):
  after = None
  if len(afters) > 0: after = J(*afters)
  assert isfile(path)
  return __FileNode(path, parent, after, logger)
