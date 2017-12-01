import distutils.util

def parse_boolean(val, default=False):
  try:
    return bool(distutils.util.strtobool(val))
  except Exception as e:
    return default
  return default
