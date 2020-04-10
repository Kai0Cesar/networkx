from heapq import heappush, heappop
from itertools import count

import networkx as nx

__all__ = ['greedy_path',]

def greedy_path(G, source, target, heuristic=None, weight='weight'):
    
    if source not in G or target not in G:
       msg = 'Either source {source} or target {target} is not in G'
       raise nx.NodeNotFound(msg)

    push = heappush
    pop = heappop

    c = count()

    #Priority, node, cost to reach and parent
    queue = [(0, next(c), source, None)]

    # Maps enqueued nodes to distance of discovered paths and the
    # computed heuristics to target.
    enqueued = {}
    # Maps explored nodes to parent closest to the source.
    explored = {}

    while queue:
        #Pop the smallest item from queue
        _, __, curnode, parent = pop(queue)

        if curnode == target:
            path = [curnode]
            node = parent
            while node is not None:
                path.append(node)
                node = explored[node]
            path.reverse()
            return path
        
        if curnode in explored:
            #Do not override the parent of starting node
            if explored[curnode] is Node:
                continue

        explored[curnode] = parent

        for neighbor in G[curnode].items()
            if neighbor in enqueued:
                continue
            else:
                h = heuristic(neighbor, target)
            enqueued[neighbor] = h
            push(queue, (h, next(c), neighbor, curnode)
    
    raise nx.NetworkXNoPath(f"Node {target} not reachable from {source}")
            

        
    
    