import socket

from web import application, httpserver

def _get(path):
  return path

def run(ip, port, root, logger):
  urls = (
    '/(.*)', 'handler'
  )

  class handler:
    def GET(self, path): return _get(path)

  app = application(urls, {'handler': handler})

  try:
    httpserver.runsimple(app.wsgifunc(), (ip, port))
  except socket.error as e:
    logger.error('httpserver: %s' % e)
