"""
    Implementation of Hash Tables
"""

class HashTable(object):
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        """
        Insert key,data into Hash table

        :param key:
        :param data:
        :return:
        """
        hashValue = self.hashfunction(key, len(self.slots))

        if self.slots[hashValue] is None:
            self.slots[hashValue] = key
            self.data[hashValue] = data

        else:
            if self.slots[hashValue] == key:
                self.data[hashValue] = data
            else:
                nextSlot = self.rehash(hashValue, len(self.slots))
                while self.slots[nextSlot] is not None and self.slots[nextSlot] != key:
                    nextSlot = self.rehash(nextSlot, len(self.slots))

                if self.slots[nextSlot] is None:
                    self.slots[nextSlot] = key
                    self.data[nextSlot] = data
                else:
                    self.data[nextSlot] = data

    @staticmethod
    def hashfunction(key, size):
        """
        Remainder type hash function

        :param key:
        :param size:
        :return:
        """
        return key % size

    @staticmethod
    def rehash(oldHash, size):
        """
        To insert into next slot if same reminder

        :param oldHash:
        :param size:
        :return:
        """
        return (oldHash+1) % size

    def get(self, key):
        """
        Get item in Hash Table at key

        :param key:
        :return:
        """
        startSlot = self.hashfunction(key, len(self.slots))
        data = None
        stop = False
        found = False
        pos = startSlot

        while self.slots[pos] is not None and not found and not stop:
            if self.slots[pos] == key:
                found = True
                data = self.data[pos]

            else:
                pos = self.rehash(pos, len(self.slots))
                if pos == startSlot:
                    stop = True

        return data

    def __getitem__(self, item):
        return self.get(item)

    def __setitem__(self, key, value):
        self.put(key, value)


if __name__ == '__main__':
    h = HashTable(5)
    h[1] = 1
    h[2] = 2
    h[3] = 3

    print(h[1])
    print(h[2])
    print(h[3])
