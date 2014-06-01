from os.path import abspath

from nodes import forbidden_response

class Handler(object):
  def __init__(self, root, logger):
    self.__root = root
    self.__logger = logger

  def __call__(self):
    return self

  def __do(self, method, path):
    return self.__root.resolve(path)(method)

  def GET(self, path):    return self.__do('GET', path)
  def PUT(self, path):    return self.__do('PUT', path)
  def POST(self, path):   return self.__do('POST', path)
  def DELETE(self, path): return self.__do('DELETE', path)