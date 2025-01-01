# There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph. The nodes are numbered from 0 to n - 1.
# Return the total number of connected components in that graph.

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Step 1: Initialize parent and rank arrays
        par = [i for i in range(n)]  # Each node is its own parent initially
        rank = [1] * n  # Each node has a rank of 1 initially

        # Step 2: Find parent of a node
        def find(n1):
            res = n1
            while res != par[res]:  # Result is not the parent of itself then stop the lopp, until then go on, we going up the tree to find the parent
                par[res] = par[par[res]]  # Path compression for efficiency: if grandparent exists then do this, or else it will be ignored
                res = par[res] # current node is the parent and keep going up thru loop
            return res # return root parent

        # Step 3: Union operation with rank optimization
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)  # Find the parents of both nodes which is set as p1 and p2

            if p1 == p2:  # If they are the same parent, do nothing
                return 0 # union not performed since they the same

            # Attach the smaller tree under the larger tree
            if rank[p2] > rank[p1]:
                par[p1] = p2 # p2 is the parent of p1 now since p2 is larger
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]

            return 1  # Return 1 to indicate a successful union

        # Step 4: Process all edges and reduce the number of components
        res = n  # Initially, every node is its own component, so we can return the number of connected nodes
        for n1, n2 in edges: #go thru each node in an edge like [1,2], [2,3]
            res -= union(n1, n2)  # Reduce components for each successful union cuz we connecting them by union

        return res  # Return the total number of components
