from os.path import abspath, isdir, isfile

from web import notfound, forbidden

from utils import J

class Node(object):
  def __init__(self, path, logger):
    self.__logger = logger
    self.__path = abspath(path)

  @property
  def path(self):
    return self.__path

  @property
  def logger(self):
    return self.__logger

  def execute(self, method):
    raise NotImplementedError()

  def forbidden(self):
    return forbidden_node(self.path, self.__logger)

class __MissingNode(Node):
  def __init__(self, path, logger):
    Node.__init__(self, path, logger)

  def execute(self, method):
    notfound()
    return "not found"

def missing_node(path, logger):
  return __MissingNode(path, logger)

class __ForbiddenNode(Node):
  def __init__(self, path, logger):
    Node.__init__(self, path, logger)

  def execute(self, method):
    forbidden()
    return "forbidden"

def forbidden_node(path, logger):
  return __ForbiddenNode(path, logger)

class __FileNode(Node):
  def __init__(self, path, after, logger):
    Node.__init__(self, path, logger)
    self.__after = after

  def execute(self, method):
    return '%s: %s' % (self.path, self.__after)

def file_node(path, afters, logger):
  after = None
  if len(afters) > 0:
    after = J(*afters)
  assert isfile(path)
  return __FileNode(path, after, logger)

class __DirNode(Node):
  def __init__(self, path, logger):
    Node.__init__(self, path, logger)

  def execute(self, method):
    return self.path

def dir_node(path, logger):
  return isdir(path) and __DirNode(path, logger) or forbidden_node(path, logger)