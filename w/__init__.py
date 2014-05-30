from web import application, httpserver

def _get(path):
  return path

def run(ip, port, root):
  urls = (
    '/(.*)', 'handler'
  )

  class handler:
    def GET(self, path): return _get(path)

  app = application(urls, {'handler': handler})
  httpserver.runsimple(app.wsgifunc(), (ip, port))
