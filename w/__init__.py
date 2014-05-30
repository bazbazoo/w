import socket

from web import application, httpserver

from handler import Handler

def run(ip, port, root, logger):
  urls = (
    '/(.*)', 'handler'
  )

  handler = Handler(root, logger)

  app = application(urls, {'handler': handler})

  try:
    httpserver.runsimple(app.wsgifunc(), (ip, port))
  except socket.error as e:
    logger.error('httpserver: %s' % e)
