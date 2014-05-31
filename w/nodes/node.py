from os.path import abspath

class Node(object):
  def __init__(self, path, parent, logger = None):
    self.__logger = logger or parent.logger
    self.__path = abspath(path)
    self.__parent = parent

  @property
  def parent(self):
    return self.__parent

  @property
  def path(self):
    return self.__path

  @property
  def logger(self):
    return self.__logger

  def resolve(self, path):
    raise NotImplementedError()

  def __call__(self, method):
    raise NotImplementedError()
