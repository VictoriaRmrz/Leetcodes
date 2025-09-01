import random
class RandomizedSet(object):

    def __init__(self):
        self.list = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.list:
            return False
        self.list.append(val)
        return True        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if not val in self.list:
            return False
        self.list.remove(val)
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.list)

def main():
    randomized_set = RandomizedSet()
    print(randomized_set.insert(1))  # True
    print(randomized_set.remove(2))   # False
    print(randomized_set.insert(2))   # True
    print(randomized_set.getRandom()) # 1 or 2

if __name__ == "__main__":
    main()