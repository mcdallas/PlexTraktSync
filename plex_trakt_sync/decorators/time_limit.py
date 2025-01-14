from functools import wraps

from plex_trakt_sync.config import TRAKT_POST_DELAY
from plex_trakt_sync.timer import Timer

timer = Timer(TRAKT_POST_DELAY)


def time_limit():
    """
    Throttles calls not to be called more often than TRAKT_POST_DELAY
    """

    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            timer.wait_if_needed()
            return fn(*args, **kwargs)

        return wrapper

    return decorator
