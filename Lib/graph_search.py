# enumerates every node reachable from root s. Can be modified to find a certain elem.
def breadth_first_search(s: str, adj: dict):
    parent = {s: None}
    level = {s: 0}
    i = 1
    frontier = [s]
    while frontier:
        next_nodes = []
        for u in frontier:
            for v in adj[u].keys():
                if v not in level.keys():
                    level[v] = i
                    parent[v] = u
                    next_nodes.append(v)
                    print(f"{u} -> {v}")
        frontier = next_nodes
        i += 1
    return parent


def depth_first_search(s, adj):
    parent = {s: None}

    def dfs_visit(u):
        for v in adj[u].keys():
            if v not in parent.keys():
                parent[v] = u
                print(f"{u} -> {v}")
                dfs_visit(v)

    dfs_visit(s)
    return parent


def dijkstra(q, adj):  # O(V^2 + E) complexity since a dict is used as the priority queue (q).
    s = {}
    while q:
        temp = min(q.values())
        nearest_node = next(k for k, v in q.items() if v == temp)
        s[nearest_node] = q.pop(nearest_node)
        for k, v in adj[nearest_node].items():
            if k in q.keys() and q[k] > s[nearest_node] + v:
                q[k] = s[nearest_node] + v
    return s
