import networkx as nx
import sys
from collections import deque
import community as cm
from collections import defaultdict
import matplotlib.pyplot as plt


# calculate the betweeness
def cal_betweeness(graph):
    all_betweenness = {}
    for edge in graph.edges():
        all_betweenness[edge] = 0

    for node in graph.nodes():
        vertex = node
        visited = set()
        visited.add(vertex)
        to_visit = deque(graph.neighbors(vertex))
        nodes = {}
        level = 1
        nodes[vertex]=0
        for item in to_visit:
            # key:node, value:level
            nodes[item] = level

        while (to_visit):
            start_node = to_visit.popleft()
            visited.add(start_node)
            all_neighbors = graph.neighbors(start_node)
            neighbors =[]
            # find unvisited neighbors
            for item in all_neighbors:
                if item not in visited and item not in to_visit:
                    neighbors.append(item)
                    level = nodes[start_node] + 1
                    nodes[item] = level
            # add neighbors to to_visited
            for item2 in neighbors:
                to_visit.append(item2)

        lowest_level = 0
        for k,v in nodes.items():
            if lowest_level<v:
                lowest_level=v

        edges={}
        nodes_value ={}
        for i_node,value in nodes.items():
            nodes_value[i_node]=1

        #assign value, iterate every level
        for i in range(lowest_level,0,-1):
            nodes_lvl = [] #nodes of each level
            for k1,v1 in nodes.items():
                if v1==i:
                    nodes_lvl.append(k1)
            for node_lvl in nodes_lvl:
                parents =[]
                node_neighbors = graph.neighbors(node_lvl)
                for node_neighbor in node_neighbors:
                    if nodes[node_neighbor]==nodes[node_lvl]-1:
                        parents.append(node_neighbor)
                weight = nodes_value[node_lvl]/len(parents)
                for parent in parents:
                    nodes_value[parent]+= weight
                    edges[(node_lvl,parent)] = edges.setdefault((node_lvl,parent),0) + nodes_value[node_lvl]

        for k3,v3 in edges.items():
            for k4,v4 in all_betweenness.items():
                if k3==k4 or (k3[1] == k4[0] and k3[0] == k4[1]):
                    all_betweenness[k4] += v3/2.0
        for item in graph.edges(data=True):
            item[2]["edge"] = all_betweenness[(item[0], item[1])]
    return graph
    # calculating the betweeness ends here


def remove(graph_b):
    graph_a = cal_betweeness(graph_b)
    items = graph_a.edges(data=True)
    sort_items = sorted(items, key=lambda item: item[2]["edge"], reverse=True)
    # print "sort_items", sort_items
    remove_v = sort_items[0][2]["edge"]
    # print "remove_v", remove_v
    r_s_item = []
    for s_item in sort_items:
        if s_item[2]["edge"] == remove_v:
            # print s_item
            r_s_item.append(s_item)
    for r in r_s_item:
        graph_a.remove_edge(r[0], r[1])
        sort_items.remove(r)
    return graph_a


if __name__ == '__main__':
    input_txt = sys.argv[1]
    output = sys.argv[2]
    G = nx.read_edgelist(input_txt, nodetype=int, data=(('edge', 0.0),))
    original_G = nx.read_edgelist(input_txt, nodetype=int, data=(('edge', 0.0),))
    mods = []
    original_partition = {}
    for node_X in original_G.nodes():
        original_partition[node_X] = 0
    original_mod = cm.modularity(original_partition,original_G)
    mods.append([original_mod,original_partition])
    while nx.number_connected_components(G) != len(original_G.nodes()):
        remove(G)
        subgraphs = nx.connected_components(G)
        partitions = {}
        num_sub = 0
        for subgraph_set in subgraphs:
            num_sub += 1
            for sub_g_node in subgraph_set:
                partitions[sub_g_node] = partitions.setdefault(sub_g_node,-1) + num_sub
        mod = cm.modularity(partitions, original_G)
        # print "mod",mod
        # print "nx.number_connected_components(G)",nx.number_connected_components(G)
        mods.append([mod, partitions])

    mods_item = sorted(mods,key=lambda x: x[0],reverse=True)
    #the best partition,key:node, value:community number
    com_dic = mods_item[0][1]
    # draw graph
    values = [com_dic.get(node) for node in G.nodes()]
    spring_layout_G = nx.spring_layout(original_G)
    nx.draw_networkx(original_G,pos=spring_layout_G,cmap=plt.get_cmap('jet'), node_color=values)
    G2 = nx.cubical_graph(original_G)
    pos = nx.spring_layout(G2)
    limits = plt.axis('off')
    plt.draw()
    plt.savefig(output)
    #covert best partition to community list
    best_com = defaultdict(list)
    for key, value in sorted(com_dic.iteritems()):
        best_com[value].append(key)

    best_com_list = []
    for k4,v4 in best_com.items():
        best_com_list.append(v4)
    for best_i in best_com_list:
        print best_i
