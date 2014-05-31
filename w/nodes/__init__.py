from forbidden import ForbiddenNode
from file import FileNode
from dir import DirNode, node
from missing import MissingNode
from base_node import Node

from os.path import isdir, isfile

def forbidden_node(path, parent):
  return ForbiddenNode(path, parent)

def to_forbidden_node(node):
  return forbidden_node(node.path, node.parent)

def root_node(path, logger):
  return node(path, Node(path, None, logger))