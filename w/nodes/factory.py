from os import access, X_OK
from os.path import isdir, isfile

from cgi import CGINode
from dir import DirNode
from missing import MissingNode
from node import Node
from file import FileNode

def node(path, parent):
  if isdir(path):
    node_type = DirNode
  elif isfile(path):
    if access(path, X_OK):
      node_type = CGINode
    else:
      node_type = FileNode
  else:
    node_type = MissingNode

  return node_type(path, parent)

def root_node(path):
  return node(path, None)