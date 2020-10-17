
"""
Application portion of Module 1
Imports physics citation graph 
"""


import urllib
import random
from matplotlib import pyplot as plt

def compute_in_degrees(digraph):
    """
    Input:
        digraph - a directed graph, represented as a dictionary
    Output:
        a dictionary - the keys are same as in digraph, 
                       the values are indegree of the key
    """
    ans = {}
    for key in digraph:
        count = 0
        for value in digraph.values():
            if key in value:
                count += 1
        ans[key] = count
    return ans

def compute_in_degrees_2(nodes, edges):
    """
    Input:
        nodes, edges
    Output:
        a dictionary - the keys are same as in digraph, 
                       the values are indegree of the key
    """
    ans = {node: 0 for node in nodes}
    for edge in edges:
        ans[edge[1]] += 1
    return ans

def in_degree_distribution(digraph):
    """
    Input:
        digraph - a directed graph, represented as a dictionary
    Output:
        a dictionary - the keys are indgrees of the nodes in digraph,
                       the values are number of nodes in digraph with that value
                       of indegree
    """
    ans = {}
    in_degree_map = compute_in_degrees(digraph)
    num_nodes = len(in_degree_map)
    value_list = list(in_degree_map.values())
    for value in value_list:
        count = value_list.count(value)
        ans[value] = count/num_nodes
    return ans

def in_degree_distribution_2(nodes, edges):
    """
    Input:
        nodes and edges
    Output:
        a dictionary - the keys are indgrees of the nodes in digraph,
                       the values are number of nodes in digraph with that value
                       of indegree
    """
    ans = {}
    in_degree_map = compute_in_degrees_2(nodes, edges)
    num_nodes = len(in_degree_map)
    value_list = list(in_degree_map.values())
    for value in value_list:
        count = value_list.count(value)
        ans[value] = count/num_nodes
    return ans

#%% question 1

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"
EX_GRAPH0 = {0: set([1, 2]), 1: set([]), 2: set([])}
EX_GRAPH1 = {0: set([1, 4, 5]), 1: set([2, 6]), 2: set([3]), 
             3: set([0]), 4: set([1]), 5: set([2]), 6: set([])}
EX_GRAPH2 = {0: set([1, 4, 5]), 1: set([2, 6]), 2: set([3, 7]), 
             3: set([7]), 4: set([1]), 5: set([2]), 6: set([]), 
             7: set([3]), 8: set([1, 2]), 9: set([0, 3, 4, 5, 6, 7])}

X = [2, 21, 5, 9, 8, 15, 6, 28, 4, 3, 1, 19, 11, 99, 13, 14, 42, 68, 17, 26, 7, 22, 40, 172, 12, 33, 10, 31, 61, 43, 37, 16, 27, 36, 111, 53, 32, 109, 23, 25, 64, 96, 91, 30, 20, 148, 24, 18, 65, 142, 57, 97, 149, 49, 45, 196, 114, 48, 41, 29, 38, 77, 74, 144, 62, 220, 70, 162, 146, 50, 34, 104, 115, 52, 92, 69, 108, 182, 186, 107, 102, 66, 63, 134, 76, 133, 75, 35, 156, 90, 54, 44, 60, 39, 79, 46, 98, 223, 59, 87, 140, 55, 194, 47, 158, 105, 113, 106, 179, 242, 81, 51, 71, 347, 100, 67, 58, 424, 73, 85, 80, 301, 86, 136, 118, 84, 94, 155, 159, 157, 101, 95, 125, 56, 110, 72, 89, 82, 205, 78, 93, 197, 112, 147, 124, 167, 230, 174, 169, 222, 129, 264, 139, 83, 88, 121, 788, 456, 2414, 116, 119, 141, 380, 191, 143, 219, 126, 373, 651, 329, 190, 180, 520, 340, 201, 406, 185, 137, 325, 252, 122, 187, 132, 183, 152, 131, 120, 494, 274, 467, 208, 217, 224, 151, 127, 153, 199, 228, 154, 164, 383, 123, 145, 1199, 265, 701, 214, 184, 438, 130, 178, 327, 177, 181, 775, 175, 273, 385, 1114, 138, 337, 192, 204, 176, 103, 189, 160, 150, 304, 212, 328, 193, 251, 232, 225, 388, 282, 213, 807, 168, 333, 1032, 135, 165, 1144, 331, 171, 211, 198, 341, 421, 240, 257, 1299, 290, 1006, 247, 308, 1641, 1775, 427, 315, 229, 475, 748, 244, 314, 268, 411, 235, 173, 295, 297, 233, 188, 117, 426, 1155, 344] 
Y = [0.09719121353979114, 0.006661865322290242, 0.047785379906373784, 0.02484695714800144, 0.029672308246308968, 0.011595246669067338, 0.04097947425279078, 0.004969391429600288, 0.05898451566438603, 0.07180410514944184, 0.1363701836514224, 0.009002520705797623, 0.01897731364782139, 0.00032409074540871443, 0.01609650702196615, 0.014728123874684912, 0.001908534389629096, 0.0008642419877565718, 0.009866762693554194, 0.004609290601368383, 0.03244508462369464, 0.006661865322290242, 0.0018725243068059057, 0.00021606049693914295, 0.01739287000360101, 0.0031688872884407635, 0.021281958948505583, 0.0031688872884407635, 0.0009002520705797623, 0.002484695714800144, 0.0029528267915016203, 0.010550954267194814, 0.004537270435722002, 0.0023766654663305727, 0.00018005041411595248, 0.0011163125675189053, 0.0036010082823190494, 0.00028808066258552396, 0.0058336334173568595, 0.004897371263953907, 0.0009362621534029529, 0.00036010082823190496, 0.00025207057976233343, 0.004501260352898812, 0.00799423838674829, 0.00021606049693914295, 0.005761613251710479, 0.010010803024846956, 0.0008282319049333814, 0.00021606049693914295, 0.0010442924018725242, 0.00036010082823190496, 0.00014404033129276198, 0.0017284839755131436, 0.0020165646380986674, 0.00010803024846957148, 0.00028808066258552396, 0.0010442924018725242, 0.0025927259632697154, 0.00435722002160605, 0.002700756211739287, 0.0005401512423478574, 0.00046813107670147644, 0.00018005041411595248, 0.0010082823190493337, 7.202016564638099e-05, 0.0007922218221101909, 7.202016564638099e-05, 0.00010803024846957148, 0.0012243428159884767, 0.0024486856319769533, 0.00021606049693914295, 0.00018005041411595248, 0.0011523226503420958, 0.00036010082823190496, 0.0006841915736406194, 0.00021606049693914295, 3.6010082823190495e-05, 0.00010803024846957148, 0.00028808066258552396, 0.00032409074540871443, 0.0007562117392870003, 0.0008282319049333814, 0.00010803024846957148, 0.0006481814908174289, 0.00021606049693914295, 0.0006841915736406194, 0.0030968671227943824, 7.202016564638099e-05, 0.00021606049693914295, 0.0011883327331652864, 0.0018005041411595247, 0.0009002520705797623, 0.0023766654663305727, 0.0008642419877565718, 0.0018725243068059057, 0.00014404033129276198, 0.00014404033129276198, 0.0010442924018725242, 0.00046813107670147644, 3.6010082823190495e-05, 0.0010442924018725242, 7.202016564638099e-05, 0.0015844436442203817, 0.00010803024846957148, 0.00028808066258552396, 0.00032409074540871443, 0.00036010082823190496, 7.202016564638099e-05, 7.202016564638099e-05, 0.0004321209938782859, 0.0011883327331652864, 0.0007562117392870003, 3.6010082823190495e-05, 0.00025207057976233343, 0.0008282319049333814, 0.0009722722362261433, 3.6010082823190495e-05, 0.0006121714079942383, 0.0005041411595246669, 0.00032409074540871443, 0.00010803024846957148, 0.00025207057976233343, 0.00021606049693914295, 0.00028808066258552396, 0.00039611091105509543, 0.0006121714079942383, 0.00014404033129276198, 0.00018005041411595248, 0.00014404033129276198, 0.00032409074540871443, 0.00036010082823190496, 0.00018005041411595248, 0.0012603528988116672, 0.00018005041411595248, 0.00036010082823190496, 0.0005041411595246669, 0.0005401512423478574, 0.00014404033129276198, 0.00028808066258552396, 0.00018005041411595248, 7.202016564638099e-05, 0.00010803024846957148, 3.6010082823190495e-05, 0.00021606049693914295, 7.202016564638099e-05, 7.202016564638099e-05, 7.202016564638099e-05, 7.202016564638099e-05, 7.202016564638099e-05, 0.00018005041411595248, 3.6010082823190495e-05, 0.00014404033129276198, 0.00028808066258552396, 0.00036010082823190496, 0.00018005041411595248, 7.202016564638099e-05, 3.6010082823190495e-05, 3.6010082823190495e-05, 0.00021606049693914295, 0.00018005041411595248, 0.00014404033129276198, 7.202016564638099e-05, 7.202016564638099e-05, 0.00010803024846957148, 3.6010082823190495e-05, 0.00018005041411595248, 3.6010082823190495e-05, 3.6010082823190495e-05, 7.202016564638099e-05, 0.00010803024846957148, 3.6010082823190495e-05, 3.6010082823190495e-05, 3.6010082823190495e-05, 0.00010803024846957148, 3.6010082823190495e-05, 3.6010082823190495e-05, 0.00010803024846957148, 7.202016564638099e-05, 3.6010082823190495e-05, 0.00010803024846957148, 3.6010082823190495e-05, 3.6010082823190495e-05, 3.6010082823190495e-05, 7.202016564638099e-05, 0.00014404033129276198, 7.202016564638099e-05, 3.6010082823190495e-05, 3.6010082823190495e-05, 3.6010082823190495e-05, 7.202016564638099e-05, 3.6010082823190495e-05, 3.6010082823190495e-05, 0.00018005041411595248, 7.202016564638099e-05, 0.00010803024846957148, 3.6010082823190495e-05, 7.202016564638099e-05, 0.00014404033129276198, 0.00010803024846957148, 3.6010082823190495e-05, 0.00014404033129276198, 0.00010803024846957148, 3.6010082823190495e-05, 3.6010082823190495e-05, 3.6010082823190495e-05, 3.6010082823190495e-05, 3.6010082823190495e-05, 3.6010082823190495e-05, 3.6010082823190495e-05, 7.202016564638099e-05, 7.202016564638099e-05, 7.202016564638099e-05, 3.6010082823190495e-05, 3.6010082823190495e-05, 3.6010082823190495e-05, 3.6010082823190495e-05, 3.6010082823190495e-05, 3.6010082823190495e-05, 0.00010803024846957148, 3.6010082823190495e-05, 7.202016564638099e-05, 0.00010803024846957148, 7.202016564638099e-05, 0.00014404033129276198, 3.6010082823190495e-05, 3.6010082823190495e-05, 0.00014404033129276198, 3.6010082823190495e-05, 3.6010082823190495e-05, 7.202016564638099e-05, 7.202016564638099e-05, 3.6010082823190495e-05, 0.00010803024846957148, 3.6010082823190495e-05, 3.6010082823190495e-05, 7.202016564638099e-05, 3.6010082823190495e-05, 3.6010082823190495e-05, 3.6010082823190495e-05, 3.6010082823190495e-05, 3.6010082823190495e-05, 3.6010082823190495e-05, 3.6010082823190495e-05, 3.6010082823190495e-05, 3.6010082823190495e-05, 7.202016564638099e-05, 3.6010082823190495e-05, 3.6010082823190495e-05, 3.6010082823190495e-05, 3.6010082823190495e-05, 3.6010082823190495e-05, 7.202016564638099e-05, 3.6010082823190495e-05, 3.6010082823190495e-05, 3.6010082823190495e-05, 7.202016564638099e-05, 3.6010082823190495e-05, 3.6010082823190495e-05, 3.6010082823190495e-05, 3.6010082823190495e-05, 3.6010082823190495e-05, 0.00010803024846957148, 3.6010082823190495e-05, 3.6010082823190495e-05, 3.6010082823190495e-05, 3.6010082823190495e-05, 3.6010082823190495e-05, 3.6010082823190495e-05, 3.6010082823190495e-05, 7.202016564638099e-05, 3.6010082823190495e-05, 3.6010082823190495e-05, 7.202016564638099e-05, 7.202016564638099e-05, 0.00010803024846957148, 3.6010082823190495e-05, 3.6010082823190495e-05, 3.6010082823190495e-05]

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib.request.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_text = graph_text.decode("utf-8")
    graph_lines = graph_text.split('\r\n')
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

def question_1():
    """
    Run question 1
    """
# =============================================================================
#     digraph = load_graph(CITATION_URL)
# =============================================================================
# =============================================================================
#     digraph = EX_GRAPH2
# =============================================================================
# =============================================================================
#     in_degree_map = in_degree_distribution(digraph)
#     x, y = [], []
#     for key, value in in_degree_map.items():
#         if key != 0:
#             x.append(key)
#             y.append(value)
# =============================================================================
    x, y = X, Y
    plt.figure("Question 1")
    plt.clf()
    plt.scatter(x, y, s=10)
    plt.title("Citation Distribution")
    plt.xlabel("Number of Citations")
    plt.xscale("log")
    plt.ylabel("Distribution")
    plt.yscale("log")
    plt.tight_layout()
    plt.ylim(1e-05, 0)
    plt.show()

# =============================================================================
# question_1()
# =============================================================================

#%% question 2

def random_digraph(num_nodes, prob):
    """
    Parameters
    ----------
    num_nodes : number of nodes in the generated digraph
    prob : probability for each possible edge to exist

    Returns
    -------
    dictionray representation of a directed graph
    """
    node_list = list(range(num_nodes))
    digraph = {}
    for node in node_list:
        digraph[node] = set()
        for other in node_list:
            if other != node:
                a = random.random()
                if a < prob:
                    digraph[node].add(other)
    return digraph

# =============================================================================
# print(random_digraph(5, 0.5))
# =============================================================================

def question_2():
    """
    Run question 2
    """
    num_nodes = 1000
    prob = 0.9
    digraph = random_digraph(num_nodes, prob)
    in_degree_map = compute_in_degrees(digraph)
    x, y = [], []
    for key, value in in_degree_map.items():
        x.append(key)
        y.append(value)
    plt.figure("Question 2")
    plt.clf()
    plt.scatter(x, y, s=10)
    plt.title("In-degree Map")
    plt.xlabel("Node")
    plt.xscale("linear")
    plt.ylabel("Indegree")
    plt.yscale("linear")
    plt.tight_layout()
# =============================================================================
#     plt.ylim(1e-05, 0)
# =============================================================================
    plt.show()
    in_degree_map = in_degree_distribution(digraph)
    x, y = [], []
    for key, value in in_degree_map.items():
        if key != 0:
            x.append(key)
            y.append(value)
    plt.figure("Question 2")
    plt.clf()
    plt.scatter(x, y, s=10)
    plt.title("In-degree Distribution")
    plt.xlabel("In-degree")
    plt.xscale("log")
    plt.ylabel("Distribution")
    plt.yscale("log")
    plt.tight_layout()
    plt.ylim(1e-05, 0)
    plt.show()
    
# =============================================================================
# question_2()
# =============================================================================

#%% question 3

def question_3():
    """
    Returns
    -------
    num_nodes : number of nodes in the citation graph
    ave_out_degree : average out degrees
    """
    digraph = load_graph(CITATION_URL)
    num_nodes = len(digraph)
    total_out_deg = 0
    for value in digraph.values():
        total_out_deg += len(value)
    ave_out_degree = total_out_deg/num_nodes
    return num_nodes, ave_out_degree

# =============================================================================
# print(question_3())
# =============================================================================

#%% question 4

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
            if edge[1] == node:
                weights.append(node)
    return weights

def weights_update(weights, new_node, new_edges):
    """
    Parameters
    ----------
    weights : list, weight of each node
    new_edges : set of tuples, a set of new edges
    Returns
    -------
    updated weights
    """
    weights.append(new_node)
    for edge in new_edges:
        weights.append(edge[1])
    return weights

# =============================================================================
# nodes, edges = {0, 1, 2}, {(0, 1), (0, 2), (1, 0), (1, 2), (2, 1)}
# new_edges = {(3, 0), (3, 1)}
# weights = weight_nodes(nodes, edges)
# print(in_degree_map(nodes, edges))   
# print(weights)
# weights_update(weights, new_edges)
# print(weights)
# =============================================================================


def DPA_digraph_low_eff(n, m):
    """
    Parameters
    ----------
    n : int, number of nodes
    m : int, ave our degree
    Returns
    -------
    a randomly generatly digraph, number of nodes is n, ave out degree is m
    low efficiency due to repeated calling of weight_noes function
    """
    digraph = {} 
    nodes = set(range(m))
    edges = set((i, j) for i in nodes for j in nodes if j != i)
    for node in range(m, n):
        _nodes = list(nodes)      
        weights = weight_nodes(_nodes, edges)
        new_edges = set()
        for _i in range(m):
            link_node = random.choices(_nodes, weights)[0]
            new_edges.add((node, link_node))
        nodes.add(node)
        edges.update(new_edges)
    for node in nodes:
        digraph[node] = set()
        for edge in edges:
            if edge[0] == node:
                digraph[node].add(edge[1])
    return digraph

def DPA_digraph(n, m):
    """
    Parameters
    ----------
    n : int, number of nodes
    m : int, ave our degree
    Returns
    -------
    nodes: a list of nodes
    edges: a set of edges in tuple
    """
    nodes = list(range(m))
    edges = set((i, j) for i in nodes for j in nodes if j != i) 
    weights = weight_nodes(nodes, edges)
    for node in range(m, n):
        link_nodes = set()
        new_edges = set()
        for _i in range(m):
            link_node = random.choice(weights)
            link_nodes.add(link_node)
            new_edges.add((node, link_node))
        weights.append(node)
        weights.extend(list(link_nodes))
        nodes.append(node)
        edges.update(new_edges)
    return nodes, edges

# =============================================================================
# nodes, edges = DPA_digraph(1239, 3)
# print(len(edges))
# plt.figure()
# plt.clf
# x_list = nodes
# y_list = []
# for x in x_list:
#     indeg = 0
#     for edge in edges:
#         if edge[1] == x:
#             indeg += 1
#     y_list.append(indeg)
# plt.plot(x_list, y_list)
# plt.show()
# =============================================================================

def question_4():
    """
    Run question 4
    """
    n, m = 27770, 13
# =============================================================================
#     n, m = 500, 5    
# =============================================================================
    nodes, edges = DPA_digraph(n, m)
    in_deg_dict = in_degree_distribution_2(nodes, edges)
    x, y = [], []
    for key, value in in_deg_dict.items():
        if key != 0:
            x.append(key)
            y.append(value)
    plt.figure("Question 4")
    plt.clf()
    plt.scatter(x, y, s=10)
    plt.title("Indegree Distribution")
    plt.xlabel("Indegree")
    plt.xscale("log")
    plt.ylabel("Distribution")
    plt.yscale("log")
    plt.tight_layout()
    plt.ylim(1e-05, 0)
    plt.show()


# =============================================================================
# question_4()
# =============================================================================
