from pymonad.tools import curry
from collections.abc import Sequence
from typing import Callable, Iterable, TypeVar
from operator import iadd, mul
# from pymonad.maybe import Just, Maybe

D_ = TypeVar('D_')
R_ = TypeVar('R_')


@curry(2)
def my_reduce(func: Callable[[D_], R_],
              it_or_sq: Iterable[D_]) -> Callable[[D_], R_]:
    iterator = iter(it_or_sq) if isinstance(it_or_sq, Sequence) else it_or_sq
    s = next(iterator)
    for i in iterator:
        s = func(s, i)
    return s


@curry(1)
def alt_range(n):
    if n == 0:
        return range(1, 2)
    elif n % 2 == 0:
        return range(2, n + 1, 2)
    else:
        return range(1, n + 1, 2)


prod = my_reduce(mul)

if __name__ == '__main__':
    number = (1, 2, 3, 4, 5)
    print(my_reduce(iadd, number))
    max_ = my_reduce(lambda x, y: x if x > y else y)
    print(max_(number))
    # site = Maybe.apply(my_reduce).to_arguments(Just(prod))
    # print(site)
