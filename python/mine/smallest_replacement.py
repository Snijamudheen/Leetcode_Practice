'''do this in python: Two strings are given, word and substr. Some of the characters in word are a question mark (?). 
Find the lexicographically smallest string that can be obtatined by replacing '?' characters such that substr appears at least once. 
If it is not possible to do so, return "-1". A substring is a contiguous sequence of characters within a string. 
For two strings a and b of the same length, a is lexicographically smaller than b if ai < bi for some 0 <= i < abs(a), and aj = bj for all 0 <= j < i'''

def smallest_replacement(word: str, substr: str) -> str:
    # Get the lengths of word and substr.
    n = len(word)      # Total characters in 'word'
    m = len(substr)    # Total characters in 'substr'
    best = None        # This will hold our best answer (smallest valid string)

    # Try every possible starting position for 'substr' in 'word'
    # We can only start at positions 0 to n - m (inclusive)
    for i in range(n - m + 1):
        can_place = True  # Assume we can put 'substr' here
        
        # Check each character of 'substr' against the matching part of 'word'
        for j in range(m):
            # word[i + j] is where the j-th letter of substr should go.
            # It must be '?' or exactly equal to substr[j].
            if word[i + j] != '?' and word[i + j] != substr[j]:
                can_place = False  # We found a mismatch
                break  # No need to check further
        
        # If we cannot place 'substr' at this position, skip to the next position.
        if not can_place:
            continue

        # Build a candidate string based on this valid placement.
        # First, copy 'word' into a list so we can change individual characters.
        candidate = list(word)
        
        # Replace the section starting at index i with 'substr'.
        for j in range(m):
            candidate[i + j] = substr[j]
        
        # Replace every '?' with 'a' (the smallest letter) to keep it as small as possible.
        for k in range(n):
            if candidate[k] == '?':
                candidate[k] = 'a'
        
        # Join the list back into a string.
        candidate_str = "".join(candidate)

        # Update best if we haven't set it yet or if candidate_str is alphabetically smaller.
        if best is None or candidate_str < best:
            best = candidate_str

    # Return the best candidate, or "-1" if no valid candidate was found.
    return best if best is not None else "-1"
