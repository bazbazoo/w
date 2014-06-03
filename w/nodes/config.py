from os.path import isdir

from ..utils import J, is_exec_file, wexecute

class NullHooks(object):
  def _get(self, which):
    return lambda: True

  def execute(self, which):
    return self._get(which)()

  def pre(self): return self.execute("pre")

class Hooks(NullHooks):
  def __init__(self, path, parent):
    self.__parent = parent
    self.__path = path
    self.__config_path = J(path, '.w')

    self.__hooks = {
      'pre': is_exec_file(J(self.__config_path, "pre"))
    }

  def __execute(self, which):
    rc, out, err = wexecute(J(self.__config_path, which))
    if err: print err
    return { 0: True }.get(rc, False)

  def _get(self, which):
    exists = self.__hooks.get(which)
    if exists:
      return lambda: self.__execute(which)
    else:
      if self.__parent:
        return self.__parent.get(which)
      else:
        return lambda: True

class NullConfig(object):
  def __init__(self):
    self._hooks = NullHooks()

  @property
  def hooks(self):
    return self._hooks

class __Config(NullConfig):
  def __init__(self, path, parent):
    self.__parent = parent
    self._hooks = Hooks(path, parent and parent.hooks)

def load_config(path, parent_config):
  if not isdir(J(path, '.w')): return parent_config or NullConfig()
  return __Config(path, parent_config)