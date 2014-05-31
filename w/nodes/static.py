from magic import Magic, MAGIC_MIME_ENCODING
from web import forbidden, internalerror, header

from file import FileNode
from forbidden import forbidden_response

M = Magic(flags = MAGIC_MIME_ENCODING)

class StaticNode(FileNode):
  def __str__(self):
    return FileNode.__str__(self) + " (static)"

  def _PUT(self):
    # TODO
    raise NotImplementedError()

  def _POST(self):
    forbidden_response("already exists")

  def _GET(self):
    if self.readable:
      mime = M.id_filename(self.path)
      header('Content-Type', mime)

      try:
        with open(self.path, 'rb') as f:
          i = iter(lambda: f.read(1024), '')
          for b in i: yield b
      except IOError as e:
        internalerror()
    else:
      forbidden_response("not readable")