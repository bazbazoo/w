from dir import node
from node import Node

def root_node(path, logger):
  return node(path, Node(path, None, logger))