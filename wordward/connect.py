import pickle
from pathlib import Path
from sys import argv

import networkx as nx

from . import generate


def main():
    start, end = argv[1], argv[2]
    graph = load()
    for v in nx.shortest_path(graph, start, end):
        print(v)


def load() -> nx.Graph:
    pickled = Path(__file__).parent / 'graph'
    if not pickled.exists():
        generate.main()
    with (Path(__file__).parent / 'graph').open('rb') as pickled:
        return pickle.load(pickled)


if __name__ == '__main__':
    main()
