import pickle
from collections import defaultdict
from pathlib import Path
from string import ascii_lowercase

import networkx as nx

from wordward.util import concat

indices = {c: i for i, c in enumerate(ascii_lowercase)}
reverse_indices = {i: c for i, c in enumerate(ascii_lowercase)}


def main():
    words = read_file(Path(__file__).parent / 'wordlist')
    graph = build_graph(words)
    with (Path(__file__).parent / 'graph').open('wb') as record:
        pickle.dump(graph, record)


def build_graph(words):
    graph = nx.Graph()
    for cluster in concat(anagrams(words), find_adjacency(words)):
        graph.add_edges_from(nx.complete_graph(cluster).edges())
    return graph


def anagrams(words):
    groups = defaultdict(lambda: [])
    for w in words:
        letters = frozenset(w)
        groups[letters].append(w)
    return groups.values()


def find_adjacency(words):
    for i in range(4):
        tree = build_tree(words, i)
        yield from leaf_clusters(tree, i)


def build_tree(words, rotate, width=26):
    tree = empty_tree(4, width)
    for word in words:
        track = tree
        for i in range(-rotate, 3 - rotate):
            track = track[indices[word[i]]]
        track[indices[word[3 - rotate]]] = True
    return tree


def leaf_clusters(tree, rotate):
    for i, top in enumerate(tree):
        for j, mid in enumerate(top):
            for k, low in enumerate(mid):
                cluster = set()
                for l, include in enumerate(low):
                    if include:
                        cluster.add(''.join(reverse_indices[n] for n in unrotate((i, j, k, l), rotate)))
                if cluster:
                    yield cluster


def rotation_indices(rotation):
    return range(-rotation, 4 - rotation)


def unrotate(seq, rotate):
    return [seq[i] for i in rotation_indices(4 - rotate)]


def empty_tree(depth, width=26):
    if depth == 0:
        # leaves are boolean
        return False
    return [empty_tree(depth - 1, width) for _ in range(width)]


def read_file(wordfile):
    return filter(None, Path(wordfile).read_text().split())


if __name__ == '__main__':
    main()
