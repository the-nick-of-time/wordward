def concat(*iterables):
    for it in iterables:
        yield from it


def take(n, iterable):
    for _, value in zip(range(n), iterable):
        yield value
