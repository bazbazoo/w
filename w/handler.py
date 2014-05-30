from os.path import abspath

from resolver import Resolver

class Handler(object):
  def __init__(self, root, logger):
    self.__root = abspath(root)
    self.__logger = logger
    self.__resolve = Resolver(logger).resolve

  def __call__(self):
    return self

  def __do(self, method, path):
    return self.__resolve(self.__root, path)(method)

  def GET(self, path):
    return self.__do('GET', path)
