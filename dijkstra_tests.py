import pytest
from dijkstra import dijkstra

def test_single_node():
    graph = {'A': {}}
    assert dijkstra(graph, 'A') == {'A': 0}

def test_multiple_nodes():
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2},
        'C': {'A': 4, 'B': 2}
    }
    assert dijkstra(graph, 'A') == {'A': 0, 'B': 1, 'C': 3}
    assert dijkstra(graph, 'B') == {'A': 1, 'B': 0, 'C': 2}
    assert dijkstra(graph, 'C') == {'A': 3, 'B': 2, 'C': 0}

def test_empty_graph():
    graph = {}
    with pytest.raises(KeyError):
        dijkstra(graph, 'A')

def test_start_not_in_graph():
    graph = {'A': {'B': 1}}
    with pytest.raises(KeyError):
        dijkstra(graph, 'C')
