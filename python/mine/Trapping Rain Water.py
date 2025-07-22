'''Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.'''

def trap(height):
    # Start with two pointers, one at the beginning and one at the end
    left, right = 0, len(height) - 1

    # These will keep track of the highest walls seen so far on both sides
    maxLeft, maxRight = 0, 0

    # Total water trapped
    water = 0

    # Keep going until the two pointers meet
    while left < right:
        # If left wall is smaller, we deal with left side
        if height[left] < height[right]:
            # If this wall is taller than any we've seen from the left, update maxLeft
            if height[left] >= maxLeft:
                maxLeft = height[left]
            else:
                # Otherwise, we can trap water here
                water += maxLeft - height[left]
            # Move the left pointer to the right
            left += 1
        else:
            # Same logic for the right side
            if height[right] >= maxRight:
                maxRight = height[right]
            else:
                water += maxRight - height[right]
            # Move the right pointer to the left
            right -= 1

    # Return the total water trapped
    return water
