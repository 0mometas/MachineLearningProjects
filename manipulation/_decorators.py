import os
import time
from datetime import timedelta
from functools import wraps, partial

from typing import Callable


def timer(func: Callable, name: str = None) -> Callable:
    """ Record Timer for any function declared this decorator. """

    @wraps(func)
    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        total_time = timedelta(seconds=round(end - start, 0))

        if name is not None:

            print("{} finished. {} hour(s) used".format(name, total_time))

        else:

            print("Finished. {} hour(s) used".format(total_time))

        return result

    return wrapper


def named_timer(name: str) -> Callable:
    """ Wrapper of Timer decorator. """

    func = partial(timer, name=name)

    return func


def create_path_if_not_exist(func: Callable) -> Callable:
    """
    Directory that pass by 'Path' as arguments will be create if not
    exists.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):

        try:

            path = kwargs["path"]

            path = os.path.dirname(path)

            if path != "":
                os.makedirs(path, exist_ok=True)

        except KeyError:
            pass

        return func(*args, **kwargs)

    return wrapper


def deco_structure(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):

        return func(*args, **kwargs)

    return wrapper


def test_deco(text: str):

    print(text)

    return None


if __name__ == "__main__":

    test_deco("Hi")
