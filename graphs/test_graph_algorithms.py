"""Run with: python3 -B -m unittest discover -s graphs -v"""

import contextlib
import io
import itertools
from pathlib import Path
import random
import runpy
import unittest


DIRECTORY = Path(__file__).resolve().parent


def load_function(filename, name):
    # The existing lab scripts print examples when loaded.
    with contextlib.redirect_stdout(io.StringIO()):
        namespace = runpy.run_path(str(DIRECTORY / filename))
    return namespace[name]


bfs = load_function('bfs.py', 'bfs')
dfs = load_function('dfs.py', 'dfs')
kruskal = load_function('kruskal.py', 'kruskal')
prims = load_function('prims.py', 'prims')
find = load_function('kruskal.py', 'find')
union = load_function('kruskal.py', 'union')


def adjacency(vertices, edges):
    graph = {v: [] for v in vertices}
    for u, v, weight in edges:
        graph[u].append((v, weight))
        graph[v].append((u, weight))
    return graph


def connected(vertices, edges):
    if not vertices:
        return True
    graph = adjacency(vertices, edges)
    seen = {vertices[0]}
    pending = [vertices[0]]
    while pending:
        for neighbour, _ in graph[pending.pop()]:
            if neighbour not in seen:
                seen.add(neighbour)
                pending.append(neighbour)
    return len(seen) == len(vertices)


class TraversalTests(unittest.TestCase):
    def setUp(self):
        self.graph = {
            'A': ['B', 'C'],
            'B': ['A', 'D'],
            'C': ['A', 'D'],
            'D': ['B', 'C'],
        }

    def test_processing_order(self):
        self.assertEqual(bfs(self.graph, 'A'), ['A', 'B', 'C', 'D'])
        self.assertEqual(dfs(self.graph, 'A'), ['A', 'B', 'D', 'C'])

    def test_repeated_calls_and_no_mutation(self):
        before = {v: list(neighbours) for v, neighbours in self.graph.items()}
        for function in (bfs, dfs):
            first = function(self.graph, 'A')
            self.assertEqual(function(self.graph, 'A'), first)
        self.assertEqual(self.graph, before)

    def test_isolated_vertex(self):
        for function in (bfs, dfs):
            self.assertEqual(function({'A': []}, 'A'), ['A'])

    def test_cycles_self_loops_and_duplicate_neighbours(self):
        graph = {'A': ['A', 'B', 'B'], 'B': ['A', 'C'], 'C': ['A', 'B']}
        for function in (bfs, dfs):
            self.assertEqual(function(graph, 'A'), ['A', 'B', 'C'])

    def test_disconnected_graph(self):
        graph = {'A': ['B'], 'B': ['A'], 'C': []}
        for function in (bfs, dfs):
            self.assertEqual(function(graph, 'A'), ['A', 'B'])


class UnionFindTests(unittest.TestCase):
    def test_find_follows_all_links(self):
        parent = {'P': 'Q', 'Q': 'R', 'R': 'R'}
        self.assertEqual(find(parent, 'P'), 'R')
        self.assertEqual(find(parent, 'R'), 'R')

    def test_union_merges_whole_groups(self):
        parent = {'A': 'A', 'B': 'A', 'C': 'C', 'D': 'C'}
        self.assertTrue(union(parent, 'B', 'D'))
        self.assertEqual(len({find(parent, v) for v in parent}), 1)
        self.assertFalse(union(parent, 'A', 'C'))
        self.assertFalse(union(parent, 'A', 'A'))


class SpanningTreeTests(unittest.TestCase):
    def assert_tree(self, vertices, edges, result, expected_weight):
        selected, total = result
        self.assertEqual(total, expected_weight)
        self.assertEqual(total, sum(weight for _, _, weight in selected))
        self.assertEqual(len(selected), len(vertices) - 1)
        self.assertTrue(connected(vertices, selected))
        # Prim may return an undirected edge in the reverse orientation.
        for u, v, weight in selected:
            self.assertTrue((u, v, weight) in edges or (v, u, weight) in edges)

    def test_prim_example_and_stale_heap_entries(self):
        vertices = ['A', 'B', 'C', 'D']
        edges = [('A', 'B', 2), ('A', 'C', 6), ('B', 'C', 3),
                 ('B', 'D', 5), ('C', 'D', 1)]
        graph = adjacency(vertices, edges)
        result = prims(graph, 'A')
        self.assertEqual(result, ([('A', 'B', 2), ('B', 'C', 3), ('C', 'D', 1)], 6))
        self.assert_tree(vertices, edges, result, 6)

    def test_kruskal_example(self):
        vertices = ['A', 'B', 'C', 'D']
        edges = [('C', 'D', 10), ('A', 'C', 3), ('A', 'B', 1), ('B', 'C', 2)]
        self.assert_tree(vertices, edges, kruskal(vertices, edges), 13)

    def test_isolated_vertex(self):
        self.assertEqual(kruskal(['A'], []), ([], 0))
        self.assertEqual(prims({'A': []}, 'A'), ([], 0))

    def test_negative_zero_and_equal_weights(self):
        vertices = ['A', 'B', 'C', 'D']
        edges = [('A', 'B', -2), ('B', 'C', 0), ('C', 'D', 1),
                 ('A', 'C', 0), ('B', 'D', 1)]
        self.assert_tree(vertices, edges, kruskal(vertices, edges), -1)
        graph = adjacency(vertices, edges)
        for start in vertices:
            self.assert_tree(vertices, edges, prims(graph, start), -1)

    def test_self_loops_and_parallel_edges(self):
        vertices = ['A', 'B']
        edges = [('A', 'A', -10), ('A', 'B', 5), ('A', 'B', 2)]
        self.assert_tree(vertices, edges, kruskal(vertices, edges), 2)
        self.assert_tree(vertices, edges, prims(adjacency(vertices, edges), 'A'), 2)

    def test_disconnected_behaviour(self):
        vertices = ['A', 'B', 'C', 'D']
        edges = [('A', 'B', 2), ('C', 'D', 3)]
        self.assertEqual(kruskal(vertices, edges), (edges, 5))
        self.assertEqual(prims(adjacency(vertices, edges), 'A'), ([('A', 'B', 2)], 2))

    def test_repeated_calls_and_no_mutation(self):
        vertices = ['A', 'B', 'C']
        edges = [('A', 'B', 4), ('B', 'C', 1), ('A', 'C', 2)]
        graph = adjacency(vertices, edges)
        before_edges = list(edges)
        before_graph = {v: list(neighbours) for v, neighbours in graph.items()}
        self.assertEqual(kruskal(vertices, edges), kruskal(vertices, edges))
        self.assertEqual(prims(graph, 'A'), prims(graph, 'A'))
        self.assertEqual(edges, before_edges)
        self.assertEqual(graph, before_graph)

    def test_small_graphs_against_exhaustive_search(self):
        rng = random.Random(42)
        for case in range(30):
            with self.subTest(case=case):
                vertices = list(range(rng.randint(2, 5)))
                pairs = {tuple(sorted((v, rng.randrange(v)))) for v in vertices[1:]}
                pairs.update(pair for pair in itertools.combinations(vertices, 2)
                             if rng.random() < 0.5)
                edges = [(u, v, rng.randint(-4, 8)) for u, v in sorted(pairs)]
                rng.shuffle(edges)
                best = min(sum(weight for _, _, weight in candidate)
                           for candidate in itertools.combinations(edges, len(vertices) - 1)
                           if connected(vertices, candidate))
                self.assert_tree(vertices, edges, kruskal(vertices, edges), best)
                graph = adjacency(vertices, edges)
                for start in vertices:
                    self.assert_tree(vertices, edges, prims(graph, start), best)


if __name__ == '__main__':
    unittest.main()
