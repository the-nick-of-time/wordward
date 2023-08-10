from src.wordward import anagrams, empty_tree, build_tree, find_adjacency


def test_anagram():
    words = ['dare', 'read', 'dear', 'make']
    assert list(anagrams(words)) == [['dare', 'read', 'dear'], ['make']]


def test_empty_tree():
    assert empty_tree(2, 2) == [[False, False], [False, False]]


def test_build_tree():
    words = ['face', 'fade', 'bade']
    tree = build_tree(words, 0, 6)
    expected = empty_tree(4, 6)
    expected[5][0][2][4] = True
    expected[5][0][3][4] = True
    expected[1][0][3][4] = True
    assert tree == expected


def test_find_adjacency():
    words = ['face', 'fade', 'bade', 'bead']
    clusters = list(find_adjacency(words))
    assert ['face', 'fade'] in clusters
    assert ['fade', 'bade'] in clusters
    assert ['bead'] in clusters
