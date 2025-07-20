'''Implement the RandomizedSet class:

RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.'''

import random
class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.val_to_index = {}

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False

        self.nums.append(val)

        final_val = len(self.nums) - 1
        self.val_to_index[val] = final_val

        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False

        idx_to_remove = self.val_to_index[val]  # val_to_index[20] = 1 
        # 10,20,30           10:0, 20:1, 30:2

        last_val = self.nums[-1]  # last_val = 30

        self.nums[idx_to_remove] = last_val  # nums[1] = 30
        # 10,30,30

        self.val_to_index[last_val] = idx_to_remove

        self.nums.pop() # 10,30

        del self.val_to_index[val] 

        return True


    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
