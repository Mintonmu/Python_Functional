from typing import Callable, Iterator, Iterable, TypeVar


D_ = TypeVar('D_')
R_ = TypeVar('R_')


def mapf(func: Callable[[D_], R_], clist: Iterable[D_]) -> Iterator[R_]:
    return (func(x) for x in clist)


if __name__ == '__main__':
    print(list(mapf(lambda x: x * 2, [1, 2, 3])))
