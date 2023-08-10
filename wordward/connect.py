import pickle
from pathlib import Path

import networkx as nx

from wordward.util import take


def main(start, end):
    graph = load()
    for v in take(2, nx.all_simple_paths(graph, start, end)):
        print(v)


def load() -> nx.Graph:
    with (Path(__file__).parent / 'graph').open('r') as pickled:
        return pickle.load(pickled)
