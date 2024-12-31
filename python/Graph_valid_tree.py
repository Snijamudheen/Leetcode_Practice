# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

class Solution:
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # Create a graph where each node is a key, and its value is a list of connected nodes
        graphMap = {}
        for i in range(n):
            graphMap[i] = []  # Start with an empty list for each node
        
        # Fill the graph with edges (connections between nodes)
        for parent, child in edges:
            graphMap[parent].append(child)  # Add the connection from parent to child
            graphMap[child].append(parent)  # Add the connection from child to parent (undirected graph so it goes both ways)

        # Keep track of nodes we've already checked
        visited = set()
        
        # This function checks if the graph has a cycle (loops back on itself)
        def isCycle(child, parent):
            # If we visit a node we've already seen, there's a cycle
            if child in visited:
                return True
            
            # Mark this node as visited
            visited.add(child)
            
            # Look at all the nodes connected to this one
            for neighbor in graphMap[child]:
                # Ignore the connection back to the node we just came from (parent)
                if neighbor == parent:
                    continue
                # If visiting a neighbor causes a cycle, return True
                if isCycle(neighbor, child):
                    return True
            
            # If no cycle is found, return False
            return False

        # Start checking for cycles from node 0
        if isCycle(0, -1):  # -1 is used as a "dummy" parent for the starting node, -1 is the parent of 0 since -1 is never reallu used
            return False  # If there's a cycle, it's not a tree
        
        # Make sure all nodes are connected (tree = no cycles + all nodes connected)
        return n == len(visited)
