from web import forbidden, internalerror

from file import FileNode
from forbidden import forbidden_response

class StaticNode(FileNode):
  def __str__(self):
    return FileNode.__str__(self) + " (static)"

  def _GET(self):
    if self.readable:
      try:
        with open(self.path, 'rb') as f:
          i = iter(lambda: f.read(1024), '')
          for b in i: yield b
      except IOError as e:
        internalerror()
    else:
      forbidden_response()