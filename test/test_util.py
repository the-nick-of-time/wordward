from wordward.util import concat, take


def test_concat():
    a = 'abc'
    b = range(1, 4)
    assert list(concat(a, b)) == ['a', 'b', 'c', 1, 2, 3]


def test_take():
    a = 'abcde'
    assert list(take(3, a)) == ['a', 'b', 'c']
    b = iter([1, 2, 3])
    assert list(take(1, b)) == [1]
