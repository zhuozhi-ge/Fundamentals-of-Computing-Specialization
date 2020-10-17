# -*- coding: utf-8 -*-
"""
Algorithmic thinking I
Application 2: Analysis of Computer Network
"""

# general imports
import urllib
import random
from collections import deque
import time
import math
import matplotlib.pyplot as plt
import example_graphs as test

# graph with 1239 nodes and 3047 edges
NETWORK_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_rf7.txt"

############################################
# Provided code

def copy_graph(graph):
    """
    Make a copy of a graph
    """
    new_graph = {}
    for node in graph:
        new_graph[node] = set(graph[node])
    return new_graph

def delete_node(ugraph, node):
    """
    Delete a node and the related edges from an undirected graph
    """
    neighbors = ugraph[node]
    ugraph.pop(node)
    for neighbor in neighbors:
        ugraph[neighbor].remove(node)
    
    
# =============================================================================
# print(targeted_order(test.GRAPH0))
# =============================================================================

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib.request.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_text = graph_text.decode("utf-8")
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print("Loaded graph with", len(graph_lines), "nodes")
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph

# =============================================================================
# graph = load_graph(NETWORK_URL)
# print(graph)
# print(sum([len(_) for _ in graph.values()])/2)
# plt.figure()
# plt.clf
# x = sorted(list(graph.keys()))
# y = [len(graph[x]) for x in graph]
# plt.plot(x, y)
# plt.show()
# =============================================================================

def ER_graph(n, p):
    """
    Parameters
    ----------
    n : int, number of nodes
    p : float, probability of each edge
    
    Returns
    -------
    nodes: a set of nodes
    edges: a set of edges in tuple
    """
    ugraph = {node: set() for node in range(n)}
    edges = [(i, j) for i in range(n) for j in range(i+1, n)]
    for edge in edges:         
        temp = random.random()
        if temp < p:
            ugraph[edge[0]].add(edge[1])
            ugraph[edge[1]].add(edge[0])
    return ugraph

# =============================================================================
# graph = ER_graph(1239, 0.003973)
# print(graph)
# print(sum([len(_) for _ in graph.values()])/2)
# plt.figure()
# plt.clf
# x = sorted(list(graph.keys()))
# y = [len(graph[x]) for x in graph]
# plt.plot(x, y)
# plt.show()
# =============================================================================

def weight_nodes(nodes, edges):
    """
    Parameters
    ----------
    nodes : set of ints, nodes
    edges : set of tuples, edges
    Returns
    -------
    a list of the weight of each node

    """
    weights = []
    for node in nodes:
        weights.append(node)
        for edge in edges:
            if node in edge:
                weights.append(node)
    return weights

# =============================================================================
# print(weight_nodes({0, 1, 2, 3}, {(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)}))
# =============================================================================

def UPA_graph(n, m):
    """
    Parameters
    ----------
    n : int, number of nodes
    m : int, ave degree
    
    Returns
    -------
    nodes: a list of nodes
    edges: a set of edges in tuple
    """
    ugraph = {node: set([i for i in range(m) if i != node]) for node in range(m)}
    weights = []
    for node, value in ugraph.items():
        weights.extend([node for _ in range(len(value)+1)])
    for node in range(m, n):
        link_nodes = set()
        for _ in range(m):
            link_node = random.choice(weights)
            ugraph[link_node].add(node) 
            link_nodes.add(link_node)
        weights.extend([node for _ in range(len(link_nodes)+1)])
        weights.extend(list(link_nodes))
        ugraph[node] = link_nodes
    return ugraph

# =============================================================================
# print(UPA_graph(5, 3))
# graph = UPA_graph(1239, 3)
# print(graph)
# print(sum([len(_) for _ in graph.values()])/2)
# plt.figure()
# plt.clf
# x = sorted(list(graph.keys()))
# y = [len(graph[x]) for x in graph]
# plt.plot(x, y)
# plt.show()
# =============================================================================
    
#%% question 1

# graph with 1239 nodes and 3047 edges
# find p
# total number of edges for ER is sum(k*p), k from 0 to n-1
# n(n-1)p/2, thus p = 0.003972926209447663 ~ 0.003972

# find m
# total number of edges for UPA is ~ n*m
# thus m = 2.459 ~ 3

def random_order(ugraph):
    """
    Parameters
    ----------
    ugraph : an undirected graph

    Returns
    -------
    a list of nodes in random order
    """
    nodes = list(ugraph.keys())
    random.shuffle(nodes)
    return nodes

# =============================================================================
# print(random_order(test.GRAPH1))
# =============================================================================

def bfs_visited(ugraph, start_node):
    """
    Find a set of node connected with start node in
    the given ugraph
    """
    queue = deque([start_node])
    visited = set([start_node])
    while queue:
        node = queue.popleft()
        for neighbor in ugraph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited

def cc_visited(ugraph):
    """
    Return a list of sets, where each set consists of
    all the nodes in a connected component
    """
    ccp = []
    nodes = set(ugraph.keys())
    while nodes:
        node = nodes.pop()
        connections = bfs_visited(ugraph, node)
        ccp.append(connections)
        nodes.difference_update(connections)
    return ccp
    
def largest_cc_size(ugraph):
    """
    Return an integer, which is the size of the
    largest connected component
    """
    size = 0
    ccp = cc_visited(ugraph)
    if ccp:
        size = max([len(_) for _ in ccp])
    return size

def compute_resilience(ugraph, attack_order):
    """
    Take a undirected graph and a list of nodes, return 
    a list of largest cc size after each removal
    """
    graph = copy_graph(ugraph)
    ans = [largest_cc_size(graph)]
    for node in attack_order:
        delete_node(graph, node)
        max_size = largest_cc_size(graph)
        ans.append(max_size)
    return ans



def question_1():
    """
    run question 1
    """
    ugraph_0 = load_graph(NETWORK_URL)
    ugraph_1 = ER_graph(1239, 0.004)
    ugraph_2 = UPA_graph(1239, 3)
    ugraphs = [ugraph_0, ugraph_1, ugraph_2]
    data = []
    for ugraph in ugraphs:
        attack_order = random_order(ugraph)
        x = list(range(len(ugraph)+1))
        y = compute_resilience(ugraph, attack_order)
        data.append((x, y))
    plt.figure()
    plt.clf
    plt.plot(data[0][0], data[0][1], "black", label="Example Compuer Network")
    plt.plot(data[1][0], data[1][1], "blue", label="ER Graph, p = 0.004")
    plt.plot(data[2][0], data[2][1], "red", label="UPA Graph, m = 3")
    plt.title("Graph resilience for random attack order")
    plt.legend(loc="upper right")
    plt.xlabel("Number of nodes removed")
    plt.ylabel("Size of largest connected component")
    plt.show()

# =============================================================================
# question_1()
# =============================================================================

#%% question 2

def question_2():
    """
    run question 2
    """
    ugraph_0 = load_graph(NETWORK_URL)
    ugraph_1 = ER_graph(1239, 0.004)
    ugraph_2 = UPA_graph(1239, 3)
    ugraphs = [ugraph_0, ugraph_1, ugraph_2]
    data = []
    for ugraph in ugraphs:
        attack_order = random_order(ugraph)
        n = len(ugraph)
        x = list(range(n//5))
        max_cc = compute_resilience(ugraph, attack_order)
        y = [(- max_cc[_x] + (n - _x))/(n - _x) for _x in x]
        data.append((x, y))
    plt.figure()
    plt.clf
    plt.plot(data[0][0], data[0][1], "black", label="Example Compuer Network")
    plt.plot(data[1][0], data[1][1], "blue", label="ER Graph, p = 0.04")
    plt.plot(data[2][0], data[2][1], "red", label="UPA Graph, m = 2")
    plt.title("Graph resilience for random attack order")
    plt.legend(loc="best")
    plt.xlabel("Number of nodes removed")
    plt.ylabel("Resilience")
    plt.show()
    
# =============================================================================
# question_2()
# =============================================================================

#%% question 3

def targeted_order(ugraph):
    """
    Compute a targeted attack order consisting
    of nodes of maximal degree
    
    Returns:
    A list of nodes, in desending order of degree
    """
    # copy the graph
    new_graph = copy_graph(ugraph)   
    order = []    
    while len(new_graph) > 0:
        max_degree = -1
        for node in new_graph:
            if len(new_graph[node]) > max_degree:
                max_degree = len(new_graph[node])
                max_degree_node = node
        order.append(max_degree_node)
        delete_node(new_graph, max_degree_node)
    return order

def fast_targeted_order(ugraph):
    """
    Compute a targeted attack order consisting
    of nodes of maximal degree
    
    Returns:
    A list of nodes, in desending order of degree
    """    
    graph = copy_graph(ugraph)
    order = []
    n = len(graph)
    degree_sets = [set() for _ in range(n)]
    for node, value in graph.items():
        deg = len(value)
        degree_sets[deg].add(node)
    for k in range(n-1, -1, -1):
        while degree_sets[k]:
            node = degree_sets[k].pop()
            for neighbor in graph[node]:
                deg_nb = len(graph[neighbor])
                degree_sets[deg_nb].remove(neighbor)
                degree_sets[deg_nb-1].add(neighbor)
            order.append(node)
            delete_node(graph, node)
    return order

# =============================================================================
# ugraph = test.GRAPH0
# print(ugraph)
# print(targeted_order(ugraph))
# print(fast_targeted_order(ugraph))
# =============================================================================

def running_time(fun, ugraph):
    """
    Parameters
    ----------
    fun : a function to generate an attack order
    ugraph : a undirected graph

    Returns
    -------
    running time of the function on the graph
    """
    start = time.time()
    fun(ugraph)
    stop = time.time()
    return stop - start

def question_3():
    """
    run question 3
    """
    x = []
    y_1 = []
    y_2 = []
    for n in range(10, 1000, 10):
        x.append(n)
        ugraph = UPA_graph(n, 5)
        y_1.append(running_time(targeted_order, ugraph))
        y_2.append(running_time(fast_targeted_order, ugraph))
    plt.figure()
    plt.clf
    plt.plot(x, y_1, "blue", label="Targeted order")
    plt.plot(x, y_2, "red", label="Fast targeted order")
    plt.title("Running time of different methods by Spyder")
    plt.legend(loc="best")
    plt.xlabel("Input size n")
    plt.ylabel("Running time (s)")
    plt.show()

# =============================================================================
# question_3()
# =============================================================================


#%% question 4

def question_4():
    """
    run question 4
    """
    ugraph_0 = load_graph(NETWORK_URL)
    ugraph_1 = ER_graph(1239, 0.004)
    ugraph_2 = UPA_graph(1239, 3)
    ugraphs = [ugraph_0, ugraph_1, ugraph_2]
    data = []
    for ugraph in ugraphs:
        attack_order = fast_targeted_order(ugraph)
        x = list(range(len(ugraph)+1))
        y = compute_resilience(ugraph, attack_order)
        data.append((x, y))
    plt.figure()
    plt.clf
    plt.plot(data[0][0], data[0][1], "black", label="Example Compuer Network")
    plt.plot(data[1][0], data[1][1], "blue", label="ER Graph, p = 0.004")
    plt.plot(data[2][0], data[2][1], "red", label="UPA Graph, m = 3")
    plt.title("Graph resilience for fast targeted attack order")
    plt.legend(loc="upper right")
    plt.xlabel("Number of nodes removed")
    plt.ylabel("Size of largest connected component")
    plt.show()
    
# =============================================================================
# question_4()
# =============================================================================


#%% question 5

def question_5():
    """
    run question 5
    """
    ugraph_0 = load_graph(NETWORK_URL)
    ugraph_1 = ER_graph(1239, 0.004)
    ugraph_2 = UPA_graph(1239, 3)
    ugraphs = [ugraph_0, ugraph_1, ugraph_2]
    data = []
    for ugraph in ugraphs:
        attack_order = fast_targeted_order(ugraph)
        n = len(ugraph)
        x = list(range(n//5))
        max_cc = compute_resilience(ugraph, attack_order)
        y = [(- max_cc[_x] + (n - _x))/(n - _x) for _x in x]
        data.append((x, y))
    plt.figure()
    plt.clf
    plt.plot(data[0][0], data[0][1], "black", label="Example Compuer Network")
    plt.plot(data[1][0], data[1][1], "blue", label="ER Graph, p = 0.04")
    plt.plot(data[2][0], data[2][1], "red", label="UPA Graph, m = 2")
    plt.title("Graph resilience for fast targeted attack order")
    plt.legend(loc="best")
    plt.xlabel("Number of nodes removed")
    plt.ylabel("Resilience")
    plt.show()
    
# =============================================================================
# question_5()
# =============================================================================
