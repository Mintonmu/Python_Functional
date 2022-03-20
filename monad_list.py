from pymonad.list import ListMonad

if __name__ == '__main__':
    print(list(range(10)), end=' ')
    print('\n')
    x = ListMonad(range(10))
    print(x[0])
