import socket

from web import application, httpserver

from handler import Handler

def run(ip, port, root, logger):
  URLS = (
    '/(.*)', 'handler'
  )

  app = application(URLS, { 'handler': Handler(root, logger) })

  try:
    httpserver.runsimple(app.wsgifunc(), (ip, port))
  except socket.error as e:
    logger.error('httpserver: %s' % e)
