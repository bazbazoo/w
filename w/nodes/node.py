from os.path import abspath

from config import load_config

class Node(object):
  def __init__(self, path, parent):
    self.__path = abspath(path)
    self.__parent = parent
    self.__config = load_config(path, parent and parent.config)

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

