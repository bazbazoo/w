from os.path import abspath

from nodes import forbidden_response

class Handler(object):
  def __init__(self, root, logger):
    self.__root = root
    self.__logger = logger

  def __call__(self):
    return self

  def __do(self, method, path):
    node = self.__root.resolve(path)

    if not abspath(node.path).startswith(self.__root.path):
      return forbidden_response()
    else:
      return node(method)

  def GET(self, path):    return self.__do('GET', path)
  def PUT(self, path):    return self.__do('PUT', path)
  def POST(self, path):   return self.__do('POST', path)
  def DELETE(self, path): return self.__do('DELETE', path)