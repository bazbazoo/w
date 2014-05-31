from os.path import abspath

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

  def __call__(self, method):
    raise NotImplementedError()
