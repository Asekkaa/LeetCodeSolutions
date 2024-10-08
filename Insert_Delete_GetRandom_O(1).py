import random

class RandomizedSet:

    def __init__(self):
        self.val_to_index = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False

        self.val_to_index[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False

        index = self.val_to_index[val]
        last_value = self.values[-1]

        # Swap the value to be removed with the last value
        self.values[index], self.values[-1] = self.values[-1], self.values[index]

        # Update the index of the last value in the dictionary
        self.val_to_index[last_value] = index

        # Remove the value from the set and list
        del self.val_to_index[val]
        self.values.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.values)
