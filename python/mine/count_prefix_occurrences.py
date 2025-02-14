# you have a list of names and a query with prefixes, Find the amount of times each prefix is used in the list of names.

def count_prefix_occurrences(names, prefixes):
    # Create a dictionary to store the count of each prefix
    prefix_count = {}

    # Loop through each prefix in the prefixes list
    for prefix in prefixes:
        count = 0  # Initialize the count to 0 for each prefix

        # Loop through each name in the names list
        for name in names:
            # Compare each name's starting characters with the prefix
            # Check if the name's first 'n' characters (where n is the length of the prefix) match the prefix
            if name[:len(prefix)] == prefix:  # This checks if the name starts with the prefix
                count += 1  # Increase the count if there's a match

        # Save the count for each prefix in the dictionary
        prefix_count[prefix] = count

    return prefix_count  # Return the final counts for all prefixes


# Example usage:
names_list = ["Alice", "Bob", "Alfred", "Albert", "Charlie", "Alexa"]
prefix_queries = ["Al", "B", "A", "C", "X"]

# Get the result from the function
result = count_prefix_occurrences(names_list, prefix_queries)

# Print the result for each prefix
for prefix, count in result.items():
    print(f"Prefix '{prefix}' appears {count} times.")
