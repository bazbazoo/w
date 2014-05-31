from os import access, R_OK, W_OK, X_OK

from web import notfound, forbidden

from node import Node

class ActualNode(Node):
  def __access(self, flag):
    return access(self.path, flag)

  @property
  def executable(self):
    return self.__access(X_OK)

  @property
  def readable(self):
    return self.__access(R_OK)

  @property
  def writable(self):
    return self.__access(W_OK)

  def _GET(self):
    raise NotImplementedError

  def _PUT(self):
    raise NotImplementedError

  def _POST(self):
    raise NotImplementedError

  def _DELETE(self):
    raise NotImplementedError

  def _INVALID(self):
    forbidden()
    return "Invalid"

  def __call__(self, method):
    return {
      'GET':    self._GET,
      'PUT':    self._PUT,
      'POST':   self._POST,
      'DELETE': self._DELETE
    }.get(method, self._INVALID)()
