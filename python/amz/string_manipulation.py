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
        self.length_map = defaultdict(deque)  # key = length, value = deque of strings

    def push(self, s: str):
        self.length_map[len(s)].append(s)

    def pop(self) -> str:
        if self.isEmpty():
            return ""

        shortest_length = min(self.length_map.keys())
        result = self.length_map[shortest_length].popleft()

        if not self.length_map[shortest_length]:
            del self.length_map[shortest_length]

        return result

    def isEmpty(self) -> bool:
        return len(self.length_map) == 0
