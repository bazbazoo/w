from os.path import abspath

from web import application

from handler import Handler
from nodes import root_node

def init_app(root, logger):
  abs_root = abspath(root)
  node = root_node(abs_root)

  URLS = ('/(.*)', 'handler')

  return application(URLS, { 'handler': Handler(node, logger) })
