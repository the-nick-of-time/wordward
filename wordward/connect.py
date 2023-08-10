import pickle
from pathlib import Path

import networkx as nx

from wordward.util import take


def main(start, end):
    graph = load()
    for v in take(2, nx.all_simple_paths(graph, start, end)):
        print(v)


def load() -> nx.Graph:
    with (Path(__file__).parent / 'graph').open('rb') as pickled:
        return pickle.load(pickled)


if __name__ == '__main__':
    from sys import argv

    main(argv[1], argv[2])
