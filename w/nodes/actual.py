from web import internalerror

from common import protected
from node import Node

class ActualNode(Node):

  def _GET(self):
    raise NotImplementedError

  def _PUT(self):
    raise NotImplementedError

  def _POST(self):
    raise NotImplementedError

  def _DELETE(self):
    raise NotImplementedError

  @protected
  def __call__(self, method):
    return {
      'GET':    self._GET,
      'PUT':    self._PUT,
      'POST':   self._POST,
      'DELETE': self._DELETE
    }.get(method, internalerror)()
