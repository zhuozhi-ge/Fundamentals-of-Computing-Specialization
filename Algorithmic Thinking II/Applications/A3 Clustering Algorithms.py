# -*- coding: utf-8 -*-

"""
Student template code for Project 3
Student will implement five functions:

slow_closest_pair(cluster_list)
fast_closest_pair(cluster_list)
closest_pair_strip(cluster_list, horiz_center, half_width)
hierarchical_clustering(cluster_list, num_clusters)
kmeans_clustering(cluster_list, num_clusters, num_iterations)

where cluster_list is a 2D list of clusters in the plane
"""

import math
import alg_cluster
import random
import urllib
import time
import matplotlib.pyplot as plt


######################################################
# Code for closest pairs of clusters

def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function that computes Euclidean distance between two clusters in a list

    Input: cluster_list is list of clusters, idx1 and idx2 are integer indices for two clusters
    
    Output: tuple (dist, idx1, idx2) where dist is distance between
    cluster_list[idx1] and cluster_list[idx2]
    """
    return (cluster_list[idx1].distance(cluster_list[idx2]), min(idx1, idx2), max(idx1, idx2))


def slow_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (slow)

    Input: cluster_list is the list of clusters
    
    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.       
    """
    ans = (float("inf"), -1, -1)
    size = len(cluster_list)
    for idx1 in range(size):
        for idx2 in range(idx1+1, size):
            temp = pair_distance(cluster_list, idx1, idx2)
            if temp[0] < ans[0]:
                ans = temp
    return ans


def fast_closest_pair(cluster_list):
    """
    Compute the distance between the closest pair of clusters in a list (fast)

    Input: cluster_list is list of clusters SORTED such that horizontal positions of their
    centers are in ascending order
    
    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] have minimum distance dist.       
    """
# =============================================================================
#     cluster_list.sort(key = lambda cluster: cluster.horiz_center())
# =============================================================================
    size = len(cluster_list)
    if size < 4:
        return slow_closest_pair(cluster_list)
    mid_idx = size//2
    l_dist = fast_closest_pair(cluster_list[:mid_idx])
    _r_dist = fast_closest_pair(cluster_list[mid_idx:])
    r_dist = (_r_dist[0], _r_dist[1]+mid_idx, _r_dist[2]+mid_idx)
    if l_dist[0] < r_dist[0]:
        ans = l_dist
    else:
        ans = r_dist
    mid_center = (cluster_list[mid_idx-1].horiz_center() + 
                  cluster_list[mid_idx].horiz_center())/2
    half_width = min(l_dist[0], r_dist[0])
    m_dist = closest_pair_strip(cluster_list, mid_center, half_width)
    if m_dist[0] < ans[0]:
        ans = m_dist
    return ans


def closest_pair_strip(cluster_list, horiz_center, half_width):
    """
    Helper function to compute the closest pair of clusters in a vertical strip
    
    Input: cluster_list is a list of clusters produced by fast_closest_pair
    horiz_center is the horizontal position of the strip's vertical center line
    half_width is the half the width of the strip (i.e; the maximum horizontal distance
    that a cluster can lie from the center line)

    Output: tuple of the form (dist, idx1, idx2) where the centers of the clusters
    cluster_list[idx1] and cluster_list[idx2] lie in the strip and have minimum distance dist.       
    """
    ans = (float("inf"), -1, -1)
    idx_in_strip = []
    for cluster in cluster_list:
        if  - half_width <= cluster.horiz_center() - horiz_center <= half_width:
            idx_in_strip.append(cluster_list.index(cluster))
    idx_in_strip.sort(key=lambda idx: cluster_list[idx].vert_center())
    size = len(idx_in_strip)
    for idx1 in range(size-1):
        for idx2 in range(idx1+1, min(idx1+4, size)):
            dist = cluster_list[idx_in_strip[idx1]].distance(cluster_list[idx_in_strip[idx2]])
            if dist < ans[0]:
                min_idx = min(idx_in_strip[idx1], idx_in_strip[idx2])
                max_idx = max(idx_in_strip[idx1], idx_in_strip[idx2])
                ans = (dist, min_idx, max_idx)
    return ans

    
######################################################################
# Code for hierarchical clustering


def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function may mutate cluster_list
    
    Input: List of clusters, integer number of clusters
    Output: List of clusters whose length is num_clusters
    """
    cluster_list.sort(key=lambda cluster: cluster.horiz_center())
    while len(cluster_list) > num_clusters:
        pair = fast_closest_pair(cluster_list)
        idx1, idx2 =  pair[1], pair[2]
        cluster_list[idx1].merge_clusters(cluster_list[idx2])
        cluster_list.pop(idx2)
        cluster_list.sort(key=lambda cluster: cluster.horiz_center())
    return cluster_list


######################################################################
# Code for k-means clustering

    
def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters
    Note: the function may not mutate cluster_list
    
    Input: List of clusters, integers number of clusters and number of iterations
    Output: List of clusters whose length is num_clusters
    """
    temp = []
    for cluster in cluster_list:
        temp.append(cluster.copy())
    temp.sort(key=lambda _: _.total_population(), reverse=True)
    centers = [(temp[idx].horiz_center(), temp[idx].vert_center()) for idx in range(num_clusters)]
    for _ in range(num_iterations):
        ans = [alg_cluster.Cluster(set(), center[0], center[1], 0, 0) for center in centers]     
        sort = [[] for _ in centers]
        for cluster in cluster_list:
            min_dist = float("inf")
            for idx in range(num_clusters):
                dist = cluster.distance(ans[idx])
                if dist < min_dist:
                    min_dist = dist
                    close_idx = idx
            sort[close_idx].append(cluster)
        for idx in range(num_clusters):
            for cluster in sort[idx]:
                ans[idx].merge_clusters(cluster)
        centers = [(cluster.horiz_center(), cluster.vert_center()) for cluster in ans]    
    return ans


#%% question 1

def gen_random_clusters(num_clusters):
    """
    Parameters
    ----------
    num_clusters : int, number of clusters

    Returns
    -------
    a list of points randomly within square (+/-1, +/-1)
    """
    clusters = []
    for _ in range(num_clusters):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        cluster = alg_cluster.Cluster(set(), x, y, 0, 0)
        clusters.append(cluster)
    return clusters

def running_time(fun, arg):
    """
    return the running time of a function, with input arg
    """
    start = time.time()
    fun(arg)
    stop = time.time()
    return stop - start
    
def question_1():
    """
    run question 1
    """
    x = list(range(2, 201))
    y_slow = []
    y_fast = []
    for n in x:
        clusters = gen_random_clusters(n)
        time_slow = running_time(slow_closest_pair, clusters)
        y_slow.append(time_slow)
        time_fast = running_time(fast_closest_pair, clusters)
        y_fast.append(time_fast)
    plt.figure("question_1")
    plt.clf()
    plt.plot(x, y_slow, "red", label="slow cloeset pair")
    plt.plot(x, y_fast, "blue", label="fast closest pair")
    plt.title("Comparing running time of slow/fast closest pair algorithm")
    plt.xlabel("Number of clusters")
    plt.ylabel("Running time (s)")
    plt.legend(loc="best")
    plt.tight_layout()
    plt.show()    

# =============================================================================
# question_1()        
# =============================================================================


#%% questions 2, 3

"""
Example code for creating and visualizing
cluster of county-based cancer risk data

Note that you must download the file
http://www.codeskulptor.org/#alg_clusters_matplotlib.py
to use the matplotlib version of this code
"""

# Flavor of Python - desktop or CodeSkulptor
#import alg_project3_solution      # desktop project solution
import alg_clusters_matplotlib


###################################################
# Code to load data tables

# URLs for cancer risk data tables of various sizes
# Numbers indicate number of counties in data table

DIRECTORY = "http://commondatastorage.googleapis.com/codeskulptor-assets/"
DATA_3108_URL = DIRECTORY + "data_clustering/unifiedCancerData_3108.csv"
DATA_896_URL = DIRECTORY + "data_clustering/unifiedCancerData_896.csv"
DATA_290_URL = DIRECTORY + "data_clustering/unifiedCancerData_290.csv"
DATA_111_URL = DIRECTORY + "data_clustering/unifiedCancerData_111.csv"


def load_data_table(data_url):
    """
    Import a table of county-based cancer risk data
    from a csv format file
    """
    data_file = urllib.request.urlopen(data_url)
    data = data_file.read()
    data = data.decode("utf-8")
    data_lines = data.split('\n')
    print("Loaded", len(data_lines), "data points")
    data_tokens = [line.split(',') for line in data_lines]
    return [[tokens[0], float(tokens[1]), float(tokens[2]), int(tokens[3]), float(tokens[4])] 
            for tokens in data_tokens]


############################################################
# Code to create sequential clustering
# Create alphabetical clusters for county data

def sequential_clustering(singleton_list, num_clusters):
    """
    Take a data table and create a list of clusters
    by partitioning the table into clusters based on its ordering
    
    Note that method may return num_clusters or num_clusters + 1 final clusters
    """
    
    cluster_list = []
    cluster_idx = 0
    total_clusters = len(singleton_list)
    cluster_size = float(total_clusters)  / num_clusters
    
    for cluster_idx in range(len(singleton_list)):
        new_cluster = singleton_list[cluster_idx]
        if math.floor(cluster_idx / cluster_size) != \
           math.floor((cluster_idx - 1) / cluster_size):
            cluster_list.append(new_cluster)
        else:
            cluster_list[-1] = cluster_list[-1].merge_clusters(new_cluster)
            
    return cluster_list
                

#####################################################################
# Code to load cancer data, compute a clustering and 
# visualize the results


def question_2_3():
    """
    Load a data table, compute a list of clusters and 
    plot a list of clusters

    Set DESKTOP = True/False to use either matplotlib or simplegui
    """
    data_table = load_data_table(DATA_3108_URL)
    
    singleton_list = []
    for line in data_table:
        singleton_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))
        
# =============================================================================
#     cluster_list = sequential_clustering(singleton_list, 15)	
#     print("Displaying", len(cluster_list), "sequential clusters")
# =============================================================================

# =============================================================================
#     cluster_list = hierarchical_clustering(singleton_list, 15)
#     print("Displaying", len(cluster_list), "hierarchical clusters")
# =============================================================================

    cluster_list = kmeans_clustering(singleton_list, 15, 5)	
    print("Displaying", len(cluster_list), "k-means clusters")

            
    # draw the clusters using matplotlib or simplegui

    #alg_clusters_matplotlib.plot_clusters(data_table, cluster_list, False)
    alg_clusters_matplotlib.plot_clusters(data_table, cluster_list, True)  #add cluster centers
    
# =============================================================================
# question_2_3()
# =============================================================================


#%% questions 5, 6

def question_5_6():
    """
    Load a data table, compute a list of clusters and 
    plot a list of clusters

    Set DESKTOP = True/False to use either matplotlib or simplegui
    """
    data_table = load_data_table(DATA_111_URL)
    
    singleton_list = []
    for line in data_table:
        singleton_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))
        
# =============================================================================
#     cluster_list = sequential_clustering(singleton_list, 15)	
#     print("Displaying", len(cluster_list), "sequential clusters")
# =============================================================================

    cluster_list = hierarchical_clustering(singleton_list, 20)
    print("Displaying", len(cluster_list), "hierarchical clusters")

# =============================================================================
#     cluster_list = kmeans_clustering(singleton_list, 9, 5)	
#     print("Displaying", len(cluster_list), "k-means clusters")
# =============================================================================

            
    # draw the clusters using matplotlib or simplegui

    #alg_clusters_matplotlib.plot_clusters(data_table, cluster_list, False)
    alg_clusters_matplotlib.plot_clusters(data_table, cluster_list, True)  #add cluster centers

# =============================================================================
# question_5_6()
# =============================================================================
    
#%% question 7

def compute_distortion(cluster_list, data_table):
    """
    compute the distortion for a clustering of the data_table
    """
    distortion = 0
    for cluster in cluster_list:
        distortion += cluster.cluster_error(data_table)
    return distortion

def question_7():
    """
    run question 7
    """
    data_table = load_data_table(DATA_111_URL)
    singleton_list = []
    for line in data_table:
        singleton_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))   
    num_clusters = 9
    num_iterations = 5
    
# =============================================================================
#     hierarchical_list = hierarchical_clustering(singleton_list, num_clusters)
#     print("Hierarchical distortion")
#     print(compute_distortion(hierarchical_list, data_table))
# =============================================================================
    
    kmeans_list = kmeans_clustering(singleton_list, num_clusters, num_iterations)
    print("Kmeans distortion")
    print(compute_distortion(kmeans_list, data_table))
        
# =============================================================================
# question_7()
# =============================================================================

#%% question 10

def question_10():
    """
    run question 10
    """
    url_data = [DATA_111_URL, DATA_290_URL, DATA_896_URL]
    for url in url_data:
        data_table = load_data_table(url)
        start = url.rfind("_")
        stop = url.rfind(".")
        num_counties = url[start+1:stop]
        
        num_iterations = 5    
        
        x = list(range(6, 21))
        y_hcc = []
        y_km = []
        for num_clusters in x:
            singleton_list = []
            for line in data_table:
                singleton_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))   
            hcc_list = hierarchical_clustering(singleton_list, num_clusters)
            hcc_distortion = compute_distortion(hcc_list, data_table)  / (1e11)
            
            singleton_list = []
            for line in data_table:
                singleton_list.append(alg_cluster.Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))              
            y_hcc.append(hcc_distortion)
            km_list = kmeans_clustering(singleton_list, num_clusters, num_iterations)
            km_distortion = compute_distortion(km_list, data_table) / (1e11)
            y_km.append(km_distortion)
        plt.figure("question_10")
        plt.clf()
        plt.plot(x, y_hcc, "red", label="hierarchical clustering distortion")
        plt.plot(x, y_km, "blue", label="k-means clustering distortion")
        plt.title("Comparing distortion of different clusterings" 
                  + "(" + num_counties + " counties)")
        plt.xlabel("Number of output clusters")
        plt.ylabel("Distortion (e11)")
        plt.legend(loc="best")
        plt.tight_layout()
        plt.show()   


# =============================================================================
# question_10()
# =============================================================================



