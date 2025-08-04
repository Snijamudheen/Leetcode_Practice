'''You have to implement the following APIs:

void push(string s);
string pop();
bool isEmpty();

Requirements:

Return the strings by length, shorter strings first.
If the strings have the same length, return in First In First Out (FIFO) order.
'''

from collections import deque, defaultdict

class StringQueue:
    def __init__(self):
        # Create a dictionary to store queues based on string length.
        # Example: {3: deque(["hey", "wow"]), 5: deque(["hello"])}
        self.length_map = defaultdict(deque)

    def push(self, s: str):
        # Add string to the correct queue based on its length.
        # Example: push("hi") → goes into key 2 → {2: deque(["hi"])}
        self.length_map[len(s)].append(s)

    def pop(self) -> str:
        # Return and remove the next string in order:
        # - shortest string length first
        # - FIFO order within the same length

        if self.isEmpty():
            return ""

        # Find the shortest string length currently in the dictionary.
        # Example: {2: deque(["hi"]), 3: deque(["cat", "dog"])} → shortest_length = 2
        shortest_length = min(self.length_map.keys())

        # Get the first string (FIFO) from that length group
        result = self.length_map[shortest_length].popleft()  # Example: returns "hi"

        # If no more strings of that length, remove that entry
        if not self.length_map[shortest_length]:
            del self.length_map[shortest_length]

        return result

    def isEmpty(self) -> bool:
        # If there are no strings in the system, return True
        return len(self.length_map) == 0


# --- Example Walkthrough ---

# q = StringQueue()
# q.push("hi")        # length = 2 → {2: ["hi"]}
# q.push("hello")     # length = 5 → {2: ["hi"], 5: ["hello"]}
# q.push("cat")       # length = 3 → {2: ["hi"], 5: ["hello"], 3: ["cat"]}
# q.push("dog")       # length = 3 → {2: ["hi"], 5: ["hello"], 3: ["cat", "dog"]}

# q.pop() → "hi"      # shortest is length 2, FIFO → removes "hi"
# q.pop() → "cat"     # next shortest is length 3 → removes "cat"
# q.pop() → "dog"     # same length 3 → FIFO → removes "dog"
# q.pop() → "hello"   # only one left → removes "hello"
# q.pop() → ""        # nothing left, returns empty string
