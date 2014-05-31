from os.path import isdir

from actual import ActualNode
from forbidden import forbidden_node

class __DirNode(ActualNode):
  def _GET(self):
    return str(self)

  def __str__(self):
    return self.path

def dir_node(path, logger):
  return isdir(path) and __DirNode(path, logger) or forbidden_node(path, logger)