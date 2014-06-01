from magic import Magic, MAGIC_MIME_ENCODING
from web import header, data
from os import remove

from file import FileNode
from missing import MissingNode
from forbidden import forbidden_response
from ..utils import J

M = Magic(flags = MAGIC_MIME_ENCODING)

class StaticNode(FileNode):
  def __str__(self):
    return FileNode.__str__(self) + " (static)"

  def resolve(self, path):
    if path == None: return self
    return MissingNode(J(self.path, path), self)

  def _GET(self):
    mime = M.id_filename(self.path)
    header('Content-Type', mime)

    with open(self.path, 'rb') as f:
      return f.read()
