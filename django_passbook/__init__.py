VERSION = ('0', '2', '0corristo')


def get_version(*args, **kwargs):
    return '.'.join(VERSION)

__version__ = get_version()
