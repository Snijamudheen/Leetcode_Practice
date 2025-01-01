# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Initialize a map where each course points to its prerequisites but its empty rn, like this -> {0: [], 1: [], 2: [], 3: []}

        premap = {i: [] for i in range(numCourses)}

        # build prerequisites map/graph map course to prereq
        for crs, prereq in prerequisites:
            premap[crs].append(prereq)

        # Set to track visited courses during the current DFS
        visitSet = set()

        # Helper function for DFS to detect cycles
        def dfs(crs):
            # If the course is already in the current path, there's a cycle
            if crs in visitSet:
                return False

            # If the course has no prerequisites, it can be completed
            if premap[crs] == []:
                return True

            # Add the course to the current path (visitSet) if not visited
            visitSet.add(crs)

            # Check all prerequisites for the current course
            for prereq in premap[crs]:
                result = dfs(prereq)
                if result == False:  # If any prerequisite cannot be completed, return False since cycle exists
                    return False

            # Remove the course from the current path (backtracking) once we done checking the prereqs
            visitSet.remove(crs)

            # Mark the course as completed by clearing its prerequisites
            premap[crs] = []

            return True

        # Check all courses to ensure they can be completed
        for crs in range(numCourses):
            result = dfs(crs) # calling function to start looking
            if result == False:  # If any course can't be completed, return False
                return False

        return True  # If no cycles are found, all courses can be completed
