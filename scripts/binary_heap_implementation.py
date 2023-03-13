"""
    Binary Heap Implementation
"""


class BinaryHeap(object):
    """
    Initialize Binary Heap Class
    """
    def __init__(self):
        # Empty Heap is initialized with zero element at 0th index
        # This is done to simplify the calculation
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i):
        """
        Method to re-arrange the heap list from bottom to up to set invariant to true

        :param i:
        :return:
        """
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                temp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = temp

            i //= 2

    def percDown(self, i):
        """
        Method to re-arrange the heap list from up to bottom to set invariant to true

        :param i:
        :return:
        """
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = temp

            i = mc

    def minChild(self, i):
        """
        Return the minium value child of parent in Binary Heap

        :param i:
        :return:
        """
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def insert(self, val):
        """
        Insert a value in the Binary Heap

        :param val:
        :return:
        """
        self.heapList.append(val)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def deleteMin(self):
        """
        Remove the minimum value in the binary heap ie root value

        :return:
        """
        deleted = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)

        return deleted

    def buildHeap(self, fromList):
        """
        Build a heap from a given List

        :param fromList:
        :return:
        """
        i = len(fromList) // 2
        self.currentSize = len(fromList)
        self.heapList = [0] + fromList[:]

        while i > 0:
            self.percDown(i)
            i -= 1

