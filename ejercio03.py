class MinHeap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def delete_min(self):
        if self.is_empty():
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        min_val = self.heap[0]
        self.heap[0] = self.heap.pop() 
        self._heapify_down(0)
        return min_val

    def _heapify_down(self, index):
        while 2 * index + 1 < len(self.heap):  
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = left

            if right < len(self.heap) and self.heap[right] < self.heap[left]:
                smallest = right

            if self.heap[index] > self.heap[smallest]:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break

# 🧪 Test cases
def test_min_heap_delete_min():
    h = MinHeap()
    print("🧹 Test 1:", h.delete_min() is None)
    h.heap = [1]; print("🧹 Test 2:", h.delete_min() == 1 and h.heap == [])
    h.heap = [1, 3, 2]; print("🧹 Test 3:", h.delete_min() == 1 and h.heap == [2, 3])
    h.heap = [1, 3, 4, 5]; print("🧹 Test 4:", h.delete_min() == 1 and h.heap == [3, 5, 4])
    h.heap = [1, 2, 3, 4, 5]
    print("🧹 Test 5:", h.delete_min() == 1)

test_min_heap_delete_min()
