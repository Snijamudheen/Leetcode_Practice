# find the maximum number of drop points that can be covered by a single horizontal or vertical path.
# User types: 10 20 30
# input().split() → ['10', '20', '30']
# map(int, ...) → [10, 20, 30] as integers

# Step 1: Read input values (pilot gets the list of drop points)
N = int(input())  # Read the number of x-coordinates (how many drop points exist)
x_coords = list(map(int, input().split()))  # Read the x-coordinates of the drop points

M = int(input())  # Read the number of y-coordinates (should be same as N)
y_coords = list(map(int, input().split()))  # Read the y-coordinates of the drop points

# Example Walkthrough: If the user enters:
# Input:
# 5
# 2 3 2 4 2
# 5
# 2 6 5 5 8
# Then, x_coords = [2, 3, 2, 4, 2]
# And y_coords = [2, 6, 5, 5, 8]

# Step 2: Count how many times each x and y coordinate appears
x_count = {}  # Dictionary to store how many times each x value appears
y_count = {}  # Dictionary to store how many times each y value appears

# Loop through all drop points and count x and y occurrences
for i in range(N):  
    x = x_coords[i]  # Get the x-coordinate of the current drop point
    y = y_coords[i]  # Get the y-coordinate of the current drop point

    # Count x-coordinates (checking how many points share the same x)
    if x in x_count:  
        x_count[x] += 1  # If x already exists, increase its count
    else:
        x_count[x] = 1  # If it's the first time seeing this x, set count to 1

    # Count y-coordinates (checking how many points share the same y)
    if y in y_count:
        y_count[y] += 1  # If y already exists, increase its count
    else:
        y_count[y] = 1  # If it's the first time seeing this y, set count to 1

# Example Walkthrough (Counting Occurrences):
# x_count = {2: 3, 3: 1, 4: 1}  (x=2 appears 3 times, x=3 appears 1 time, x=4 appears 1 time)
# y_count = {2: 1, 6: 1, 5: 2, 8: 1}  (y=5 appears 2 times, other y's appear once)

# 🚨 This is WRONG because max(x_count) returns the largest key in the dictionary, not the largest value. so use max(x_count.values()) to get the values. cuz dict = {value:key}
# Step 3: Find the maximum number of drop points we can hit in a single straight line
max_x_path = max(x_count.values())  # The highest number of drop points in a vertical path
max_y_path = max(y_count.values())  # The highest number of drop points in a horizontal path

# Example Walkthrough (Finding the Max Path):
# max_x_path = max([3, 1, 1]) = 3 (because x=2 appears 3 times)
# max_y_path = max([1, 1, 2, 1]) = 2 (because y=5 appears 2 times)

# Step 4: Pick the best path (whichever hits the most drop points)
print(max(max_x_path, max_y_path))  # Print the highest number (best path)

# Example Walkthrough (Final Step)
# max(3, 2) = 3, so the output will be:
# Output:
# 3
