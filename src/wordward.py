from collections import defaultdict
from pathlib import Path
from string import ascii_lowercase

import networkx as nx

indices = {c: i for i, c in enumerate(ascii_lowercase)}
reverse_indices = {i: c for i, c in enumerate(ascii_lowercase)}


def anagrams(words):
    groups = defaultdict(default=[])
    for w in words:
        letters = frozenset(w)
        groups[letters].append(w)
    return list(groups.values())


def build_tree(words, rotate):
    tree = empty_tree(4)
    for word in words:
        track = tree
        for i in range(-rotate, 4 - rotate):
            track = track[indices[word[i]]]
        track = True
    return tree


def find_adjacency(words):
    clusters = []
    for i in range(4):
        tree = build_tree(words, i)
        clusters.extend(leaf_clusters(tree))
    return clusters


def leaf_clusters(tree):
    clusters = []
    for i, top in enumerate(tree):
        for j, mid in enumerate(top):
            for k, low in enumerate(mid):
                cluster = []
                for l, include in enumerate(low):
                    if include:
                        cluster.append(''.join(reverse_indices[n] for n in (i, j, k, l)))
                clusters.append(cluster)
    return clusters


def empty_tree(depth, width=26):
    if depth == 0:
        # leaves are boolean
        return False
    return [empty_tree(depth - 1) for _ in range(width)]


def read_file(wordfile):
    return filter(None, Path(wordfile).read_text().split())


def concat(*iterables):
    for it in iterables:
        yield from it


def build_graph(words):
    graph = nx.Graph()
    for cluster in concat(anagrams(words), find_adjacency(words)):
        graph.add_edges_from(nx.complete_graph(cluster).edges())
