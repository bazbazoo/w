from os.path import abspath

class Node(object):
  def __init__(self, path, parent):
    self.__path = abspath(path)
    self.__parent = parent

  @property
  def parent(self):
    return self.__parent

  @property
  def path(self):
    return self.__path

  def resolve(self, path):
    raise NotImplementedError()

  def __call__(self, method):
    raise NotImplementedError()
