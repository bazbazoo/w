from os.path import abspath

class Node(object):
  def __init__(self, path, parent, config = None):
    self.__path = abspath(path)
    self.__parent = parent
    self.__config = config or (parent and parent.config)

  @property
  def parent(self):
    return self.__parent

  @property
  def path(self):
    return self.__path

  @property
  def config(self):
    return self.__config

  def resolve(self, path):
    raise NotImplementedError()

  def __call__(self, method):
    raise NotImplementedError()

