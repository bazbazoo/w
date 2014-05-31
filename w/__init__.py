import socket
from os.path import abspath

from web import application, httpserver

from handler import Handler
from nodes import root_node

def run(ip, port, root, logger):
  abs_root = abspath(root)
  node = root_node(abs_root, logger)

  URLS = ('/(.*)', 'handler')

  app = application(URLS, { 'handler': Handler(node, logger) })

  try:
    httpserver.runsimple(app.wsgifunc(), (ip, port))
  except socket.error as e:
    logger.error('httpserver: %s' % e)
