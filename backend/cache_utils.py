import time
import functools

def ttl_cache(ttl_seconds):
    """
    Simple in-memory TTL cache decorator.
    Cached result expires after `ttl_seconds`.
    """
    def decorator(fn):
        cache = {}
        @functools.wraps(fn)
        def wrapped(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            now = time.time()
            if key in cache:
                result, expires_at = cache[key]
                if now < expires_at:
                    return result
            result = fn(*args, **kwargs)
            cache[key] = (result, now + ttl_seconds)
            return result
        return wrapped
    return decorator
