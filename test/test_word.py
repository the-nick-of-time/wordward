from pathlib import Path

import networkx as nx

from wordward.generate import anagrams, empty_tree, build_tree, find_adjacency, build_graph, leaf_clusters, read_file


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


def test_build_tree_rotated():
    words = ['face', 'fade', 'bade']
    tree = build_tree(words, 3, 6)
    expected = empty_tree(4, 6)
    expected[0][2][4][5] = True
    expected[0][3][4][5] = True
    expected[0][3][4][1] = True
    assert tree == expected


def test_find_adjacency():
    words = ['face', 'fade', 'bade', 'bead']
    clusters = list(find_adjacency(words))
    assert {'face', 'fade'} in clusters
    assert {'fade', 'bade'} in clusters
    assert {'bead'} in clusters


def test_adjacency_span():
    words = ['mace', 'face', 'mice', 'mate', 'mack']
    adjacencies = list(find_adjacency(words))
    assert {'mace', 'face'} in adjacencies
    assert {'mace', 'mice'} in adjacencies
    assert {'mace', 'mate'} in adjacencies
    assert {'mace', 'mack'} in adjacencies


def test_build_graph():
    words = ['face', 'fade', 'fare', 'bade', 'bead']
    expected = nx.Graph()
    expected.add_edges_from([
        ['face', 'fade'],
        ['face', 'fare'],
        ['fade', 'fare'],
        ['fade', 'bade'],
        ['bade', 'bead'],
    ])
    assert nx.utils.graphs_equal(expected, build_graph(words))


def test_leaf_clusters_solo():
    words = ['face', 'fade', 'bade']
    tree = build_tree(words, 0, 6)
    clusters = list(leaf_clusters(tree, 0))
    assert all(len(c) == 1 for c in clusters)
    assert len(clusters) == 3


def test_leaf_clusters():
    words = ['face', 'fade', 'bade']
    tree = build_tree(words, 1, 6)
    clusters = list(leaf_clusters(tree, 1))
    assert {'face', 'fade'} in clusters
    assert {'bade'} in clusters
    assert len(clusters) == 2


def test_wordlist():
    words = list(read_file(Path(__file__).parent.parent / 'wordward/wordlist'))
    assert len(words) == 2351
    assert all(len(w) == 4 for w in words)
