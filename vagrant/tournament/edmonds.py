#!/usr/bin/env python

class Vertex:
    def __init__(self, value):
        self.value = value
        self.edges = {}
    def degree(self):
        return len(self.edges)
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return "Vertex({})".format(repr(self.value))

class Edge:
    def __init__(self, v, w):
        self.v = v
        self.w = w
    def other(self, v):
        if v == self.v:
            return self.w
        elif v == self.w:
            return self.v
        else:
            raise
    def __str__(self):
        return "<{}, {}>".format(str(self.v), str(self.w))
    def __repr__(self):
        return "Edge({}, {})".format(repr(self.v), repr(self.w))

class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []
    def find_vertex(self, value):
        for vertex in self.vertices:
            if vertex.value == value:
                return vertex
        return None
    def find_edge(self, v, w):
        if w in v.edges:
            return v.edges[w]
        else:
            return None
    def add_edge(self, v, w):
        edge = self.find_edge(v, w)
        if not edge:
            edge = Edge(v, w)
            v.edges[w] = edge
            w.edges[v] = edge
            self.edges.append(edge)
    def remove_edge(self, v, w):
        edge = self.find_edge(v, w)
        if edge:
            del v.edges[w]
            del w.edges[v]
            self.edges.remove(edge)
    def add_vertex(self, vertex):
        self.vertices.append(vertex)
    def remove_vertex(self, vertex):
        for w in vertex.edges:
            edge = vertex.edges[w]
            self.edges.remove(edge)
            del w.edges[vertex]
        vertex.edges = []
        self.vertices.remove(vertex)
    def clone(self):
        g = Graph()
        for vertex in self.vertices:
            g.add_vertex(Vertex(vertex.value))
        for edge in self.edges:
            g.add_edge(g.find_vertex(edge.v.value), g.find_vertex(edge.w.value))
        return g
    def __str__(self):
        return '\n'.join([str(x) for x in \
            ["Graph {"] + self.vertices + self.edges + ["}"]])


class Matching(Graph):
    def augment_along(self, path):
        for edge in path.edges:
            v_vertex = self.find_vertex(edge.v.value)
            w_vertex = self.find_vertex(edge.w.value)
            assert(v_vertex is not None and w_vertex is not None)
            vw_edge = self.find_edge(v_vertex, w_vertex)
            if vw_edge:
                self.remove_edge(v_vertex, w_vertex)
            else:
                self.add_edge(v_vertex, w_vertex)
    def get_matched(self, value):
        vertex = self.find_vertex(value)
        assert(vertex is not None)
        assert(len(vertex.edges) == 1)
        for vertex in vertex.edges:
            return vertex
    @staticmethod
    def from_graph(source):
        m = Matching()
        for vertex in source.vertices:
            m.add_vertex(Vertex(vertex.value))
        return m

class Blossom():
    blossom_index = 0
    def __init__(self, v, w, tree):
        self.v = v
        self.w = w
        self.tree = tree
        self.path = None
        self.precompute_path()
        self.blossom_index = Blossom.blossom_index
        Blossom.blossom_index += 1
    def precompute_path(self):
        if self.path:
            return
        v_tree = self.tree.find(self.v)
        w_tree = self.tree.find(self.w)
        v_height = v_tree.height()
        w_height = w_tree.height()
        v_node = v_tree
        w_node = w_tree
        # Contains v, v', v'', ...
        v_value_path = []
        # Contains w, w', w'', ...
        w_value_path = []
        if v_height > w_height:
            for _ in range(v_height - w_height):
                v_value_path.append(v_node.value)
                v_node = v_node.parent
        elif w_height > v_height:
            for _ in range(w_height - v_height):
                w_value_path.append(w_node.value)
                w_node = w_node.parent
        while True:
            if v_node == w_node:
                break
            elif v_node.parent is None or w_node.parent is None:
                raise
            else:
                v_value_path.append(v_node.value)
                w_value_path.append(w_node.value)
                v_node = v_node.parent
                w_node = w_node.parent
        # Contains v, v'', v''', ... common ancestor ... w'', w', w
        self.path = v_value_path + [v_node.value] + w_value_path[::-1]
    def __str__(self):
        return "B{}".format(self.path)
    def __repr__(self):
        return "Blossom({}, {}, {})".format(self.v, self.w, self.tree)
    def contract_graph(self, graph):
        marked_vertex = Vertex("blossom-{}".format(self.blossom_index))
        connected = set()
        contraction = {}
        for node_value in self.path:
            node_vertex = graph.find_vertex(node_value)
            for connected_vertex in node_vertex.edges:
                connected.add(connected_vertex.value)
                contraction[connected_vertex.value] = node_vertex.value
            # Filter internal nodes
            if node_vertex.value in connected:
                connected.remove(node_vertex.value)
            graph.remove_vertex(node_vertex)
        graph.add_vertex(marked_vertex)
        for connected_value in connected:
            connected_vertex = graph.find_vertex(connected_value)
            assert(connected_vertex is not None)
            graph.add_edge(marked_vertex, connected_vertex)
        return contraction
    def get_path_index(self, value):
        for i in range(len(self.path)):
            if self.path[i] == value:
                return i
        return None
    def lift_path(self, path, contraction):
        incoming_edge = None
        outgoing_edge = None
        marked_value = "blossom-{}".format(self.blossom_index)
        for edge in path.edges:
            if edge.w.value == marked_value:
                incoming_edge = edge
            if edge.v.value == marked_value:
                outgoing_edge = edge

        if incoming_edge and outgoing_edge:
            incoming_edge_value = contraction[incoming_edge.v.value]
            outgoing_edge_value = contraction[outgoing_edge.w.value]
            incoming_edge_index = self.get_path_index(incoming_edge_value)
            outgoing_edge_index = self.get_path_index(outgoing_edge_value)
            if outgoing_edge_index < incoming_edge_index:
                outgoing_edge_index += len(self.path)
            # If there are an even number of vertices between the
            # outgoing path and the incoming path, the path must be
            # reversed.
            if (outgoing_edge_index - incoming_edge_index) % 2 == 0:
                increment = -1
            else:
                increment = 1
        elif incoming_edge:
            incoming_edge_value = contraction[incoming_edge.v.value]
            incoming_edge_index = self.get_path_index(incoming_edge_value)
            outgoing_edge_index = incoming_edge_value - 1 + len(self.path)
            increment = 1
        elif outgoing_edge:
            outgoing_edge_value = contraction[outgoing_edge.w.value]
            outgoing_edge_index = self.get_path_index(outgoing_edge_value)
            incoming_edge_index = outgoing_edge_value - 1
            increment = -1
        else:
            raise

        index = incoming_edge_index
        end = outgoing_edge_index
        if incoming_edge:
            previous_value = incoming_edge.v.value
        else:
            previous_value = None
        while index != end:
            if previous_value:
                path.edges.append(Edge(Vertex(previous_value), Vertex(path[index])))
            previous_value = path[index]
            index += increment
        if outgoing_edge:
            path.edges.append(Edge(Vertex(previous_value), Vertex(outgoing_edge.w.value)))
        path.edges = filter(lambda edge: (marked_value not in (edge.v.value, edge.w.value)), path.edges)

class Path:
    def __init__(self):
        self.edges = []
    def __str__(self):
        return '\n'.join([str(x) for x in \
            ["Path {"] + self.edges + ["}"]])
    
#   def discover_path(self, graph, value_start, value_end):
#       vertex_start = graph.find_vertex(value_start)
#       value_end = graph.find_vertex(value_end)
#       assert(vertex_start is not None)
#       assert(vertex_end is not None)
#       paths_start = {}
#       paths_end = {}
#       while True:
#           paths_start


class Tree:
    def __init__(self, value, children, parent):
        self.value = value
        self.children = children
        self.parent = parent
    def add_child(self, value):
        tree = Tree(value, [], self)
        self.children.append(tree)
        return tree
    def subnodes(self):
        s = [self]
        for child in self.children:
            s += child.subnodes()
        return s
    def height(self):
        if self.parent == None:
            return 0
        else:
            return 1 + self.parent.height()
    def find(self, value):
        search = [self]
        while search:
            t = search[0]
            if t.value == value:
                return t
            else:
                search += t.children
                search = search[1:]
        return None
    def root(self):
        if self.parent is None:
            return self
        else:
            return self.parent.root()
    def __str__(self):
        return "T[{} {}]".format(self.value, self.children)
    def __repr__(self):
        return "Tree({}, {})".format(self.value, self.children)

class Marked:
    def __init__(self):
        self.node_values = {}
        self.node_pairs = {}
    def append_value(self, value):
        self.node_values[value] = 1
    def append_pair(self, v, w):
        if v not in self.node_pairs:
            self.node_pairs[v] = {}
        self.node_pairs[v][w] = 1
    def has_value(self, value):
        return value in self.node_values
    def has_pair(self, v, w):
        return self.test_has_pair(v, w) or self.test_has_pair(w, v)
    def test_has_pair(self, v, w):
        return v in self.node_pairs and w in self.node_pairs[v] and self.node_pairs[v][w] == 1

        
def find_maximum_matching(graph, matching):
    path = find_augmenting_path(graph, matching)
    if path and len(path.edges) > 0:
        matching.augment_along(path)
        return find_maximum_matching(graph, matching)
    else:
        return matching

def find_unmarked_vertex_with_even_distance(forest, marked):
    """
    Returns a value from forest that is not marked and has even height
    """
    found = None
    for tree in forest:
        for subnode in tree.subnodes():
            if marked.has_value(subnode.value) or subnode.height () % 2 != 0:
                continue
            else:
                found = subnode
                break
    return found

def find_unmarked_edge_incident_on_v(v, marked):
    """
    Returns an unmarked Edge connecting 2 values, one of which is v.
    """
    for w, edge in v.edges.items():
        if marked.has_pair(v.value, w.value):
            continue
        return edge
    return None

def find_tree_in_forest(forest, value):
    for tree in forest:
        t = tree.find(value)
        if t:
            return t
    return None

def find_augmenting_path(graph, matching):
    # Trees containing values that were originally in `matching`
    forest = []

    # Values of "marked" nodes, and Edges joining 2 values of "marked" nodes
    marked = Marked()

    # Mark all edges that are already in `matching`
    for edge in matching.edges:
        marked.append_pair(edge.v.value, edge.w.value)

    # Create a singleton tree { v } for each exposed vertex `v` in `matching`
    for vertex in matching.vertices:
        assert(vertex.degree() < 2)
        if vertex.degree() == 0:
            forest.append(Tree(vertex.value, [], None))

    while True:
        v_tree = find_unmarked_vertex_with_even_distance(forest, marked)
        if not v_tree:
            break

        v_value = v_tree.value
        v_vertex = graph.find_vertex(v_value)
        while True:
            e = find_unmarked_edge_incident_on_v(v_vertex, marked)
            if not e:
                break

            # Bind `w` as the other end of edge `e`
            w_vertex = e.other(v_vertex)
            w_value = w_vertex.value

            # Find w_value in `forest`
            w_tree = find_tree_in_forest(forest, w_value)

            if w_tree is None:
                # We know that w must be matched, so add vw and wx to forest
                # where x is w's matching
                x_value = matching.get_matched(w_value).value
                w_tree = v_tree.add_child(w_value)
                x_tree = w_tree.add_child(x_value)
            else:
                if w_tree.height() % 2 == 1:
                    # Do nothing
                    pass
                else:
                    v_root = v_tree.root()
                    w_root = w_tree.root()
                    if v_root != w_root:
                        p = Path()
                        node = v_tree
                        while node.parent:
                            p.edges.append(graph.find_edge(
                                graph.find_vertex(node.value),
                                graph.find_vertex(node.parent.value)))
                            node = node.parent
                        p.edges = p.edges[::-1]
                        p.edges.append(e)
                        node = w_tree
                        while node.parent:
                            p.edges.append(graph.find_edge(
                                graph.find_vertex(node.value),
                                graph.find_vertex(node.parent.value)))
                            node = node.parent
                        return p
                    else:
                        blossom = Blossom(v_value, w_value, v_root)
                        graph_clone = graph.clone()
                        matching_clone = matching.clone()
                        contraction = blossom.contract_graph(graph_clone)
                        blossom.contract_graph(matching_clone)
                        path = find_augmenting_path(graph_clone, matching_clone)
                        blossom.lift_path(path, contraction)
                        return path
            marked.append_pair(v_value, w_value)
        marked.append_value(v_value)
    return Path()

class Tests:
    def simple(self):
        """
        A simple test

        >>> g = Graph()
        >>> g.add_vertex(Vertex(2))
        >>> g.add_vertex(Vertex(1))
        >>> g.add_vertex(Vertex(0))
        >>> g.add_vertex(Vertex(3))
        >>> g.add_edge(g.find_vertex(1), g.find_vertex(2))
        >>> g.add_edge(g.find_vertex(0), g.find_vertex(3))
        >>> g.add_edge(g.find_vertex(2), g.find_vertex(3))
        >>> m = Matching.from_graph(g)
        >>> m = find_maximum_matching(g, m)
        >>> print m
        Graph {
        2
        1
        0
        3
        <0, 3>
        <1, 2>
        }
        """
        pass
    def loop(self):
        """
        A test containing a loop
        
        >>> g = Graph()
        >>> g.add_vertex(Vertex(1))
        >>> g.add_vertex(Vertex(2))
        >>> g.add_vertex(Vertex(3))
        >>> g.add_vertex(Vertex(4))
        >>> g.add_vertex(Vertex(5))
        >>> g.add_vertex(Vertex(6))
        >>> g.add_edge(g.find_vertex(1), g.find_vertex(2))
        >>> g.add_edge(g.find_vertex(2), g.find_vertex(3))
        >>> g.add_edge(g.find_vertex(3), g.find_vertex(4))
        >>> g.add_edge(g.find_vertex(4), g.find_vertex(5))
        >>> g.add_edge(g.find_vertex(5), g.find_vertex(6))
        >>> g.add_edge(g.find_vertex(6), g.find_vertex(2))
        >>> m = Matching.from_graph(g)
        >>> m = find_maximum_matching(g, m)
        >>> print m
        Graph {
        1
        2
        3
        4
        5
        6
        <5, 6>
        <3, 4>
        <1, 2>
        }
        """
        pass

import sys

def main():
    # Secret Santa?
    g = Graph()
    g.add_vertex(Vertex("Roger"))
    g.add_vertex(Vertex("Nitin"))
    g.add_vertex(Vertex("Vincent"))
    g.add_vertex(Vertex("Allan"))
    g.add_vertex(Vertex("Gloria"))
    g.add_vertex(Vertex("Jessica"))
    g.add_vertex(Vertex("Parth"))
    g.add_vertex(Vertex("James"))
    g.add_vertex(Vertex("Sharon"))
    g.add_edge(g.find_vertex("Roger"), g.find_vertex("Nitin"))
    g.add_edge(g.find_vertex("Roger"), g.find_vertex("Vincent"))
    g.add_edge(g.find_vertex("Allan"), g.find_vertex("Vincent"))
    m = Matching.from_graph(g)
    m = find_maximum_matching(g, m)
    print m

if __name__ == '__main__':
    main()
