from functools import wraps

def log(prefix=">>> "):
  def decorate(func):
    '''
    :param func:
    :return:
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
      print "%sCalling %s: args: %s, kwargs: %s" % (prefix, func.__name__, args, kwargs)

      func(*args, **kwargs)

    return wrapper

  return decorate
