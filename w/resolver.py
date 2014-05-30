from os.path import isdir, isfile

from nodes import file_node, dir_node, forbidden_node, missing_node
from utils import S, J

class Resolver(object):
  def __init__(self, logger):
    self.__logger = logger

  def __resolve(self, rest, root = '/'):
    if len(rest) == 0:
      # Must be a directory (ended with a '/')
      return dir_node(root, self.__logger)

    next = root + rest[0]

    if rest[0] == '..':
      return forbidden_node(next, self.__logger)

    if isdir(next): # TODO: check if executable?
      return self.__resolve(root = next + '/', rest = rest[1:])
    elif isfile(next):
      return file_node(next, rest[1:], self.__logger)
    else:
      return missing_node(next, self.__logger)

  def resolve(self, root, path):
    node = self.__resolve(rest = S(J(root, path)))
    if len(node.path) < len(root):
      return node.forbidden()
    else:
      return node
