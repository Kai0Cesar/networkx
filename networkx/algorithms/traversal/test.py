import networkx as nx 

def main(graph):

    graph.add_edge('A','B')
    graph.add_edge('A','C')
    graph.add_edge('B','D')
    graph.add_edge('B','E')
    graph.add_edge('C','F')
    graph.add_edge('C','G')

    list(nx.bfs_edges(graph,source='A'))
