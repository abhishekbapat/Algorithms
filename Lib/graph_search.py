# enumerates every node reachable from root s. Can be modified to find a certain elem.
def breadth_first_search(s, adj):
    parent = {s: None}
    level = {s: 0}
    i = 1
    frontier = [s]
    while frontier:
        next_nodes = []
        for u in frontier:
            for v in adj[u]:
                if v in level:
                    level[v] = i
                    parent[v] = u
                    next_nodes.append(v)
        frontier = next_nodes
        i += 1
    return parent
