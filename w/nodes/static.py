from magic import Magic, MAGIC_MIME_ENCODING
from web import forbidden, internalerror, header

from file import FileNode
from forbidden import forbidden_response

magic = Magic(flags = MAGIC_MIME_ENCODING)

class StaticNode(FileNode):
  def __str__(self):
    return FileNode.__str__(self) + " (static)"

  def _GET(self):
    if self.readable:
      mime = magic.id_filename(self.path)
      header('Content-Type', mime)

      try:
        with open(self.path, 'rb') as f:
          i = iter(lambda: f.read(1024), '')
          for b in i: yield b
      except IOError as e:
        internalerror()
    else:
      forbidden_response()