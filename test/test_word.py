from src.wordward import anagrams, empty_tree


def test_anagram():
    words = ['dare', 'read', 'dear', 'make']
    assert list(anagrams(words)) == [['dare', 'read', 'dear'], ['make']]


def test_empty_tree():
    assert empty_tree(2, 2) == [[False, False], [False, False]]
