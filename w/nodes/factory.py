from os import access, X_OK
from os.path import isdir, isfile

from cgi import CGINode
from dir import DirNode
from missing import MissingNode
from node import Node
from static import StaticNode

def node(path, parent):
  if isdir(path):
    node_type = DirNode
  elif isfile(path):
    if access(path, X_OK):
      node_type = CGINode
    else:
      node_type = StaticNode
  else:
    node_type = MissingNode

  return node_type(path, parent)

def root_node(path, logger):
  return node(path, Node(path, None, logger))