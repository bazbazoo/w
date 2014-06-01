from magic import Magic, MAGIC_MIME_ENCODING
from web import header, data
from os import remove

from actual import ActualNode
from missing import MissingNode
from forbidden import forbidden_response
from ..utils import J

M = Magic(flags = MAGIC_MIME_ENCODING)

class FileNode(ActualNode):
  def resolve(self, path):
    if path == None: return self
    return MissingNode(J(self.path, path), self)

  def _GET(self):
    mime = M.id_filename(self.path)
    header('Content-Type', mime)

    with open(self.path, 'rb') as f:
      return f.read()

  def _DELETE(self):
    remove(self.path)

  def _PUT(self):
    with open(self.path, 'wb') as f:
      f.write(data())

  def _POST(self):
    return forbidden_response("already exists")
