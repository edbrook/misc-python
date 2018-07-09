class Queue:
    def __init__(self, capacity=0):
        if capacity < 0:
            raise ValueError("Capacity must be >= 0 [0 = no limit]")
        self._head = None
        self._tail = None
        self._capacity = capacity
        self._size = 0
    
    def add(self, value):
        if self._tail is None:
            self._tail = self._head = _Entry(value)
            self._size += 1
        else:
            new_entry = _Entry(value)
            
            if self._tail is not None:
                new_entry.prev = self._tail
                self._tail.next = new_entry

            self._tail = new_entry
            
            if self._head is None:
                self._head = self._tail

            self._size += 1

        self._trim_to_capacity()
        
    def remove(self):
        if self._size <= 0:
            raise IndexError("No entries in the queue")
        value = self._head.value
        if self._tail == self._head:
            self._tail = self._head = None
        else:
            self._head = self._head.next
        self._size -= 1
        return value
    
    def _trim_to_capacity(self):
        if self._capacity > 0 and self._size > self._capacity:
            if self._tail == self._head:
                self._tail = self._head = None
            else:
                if self._head.next is not None:
                    self._head.next.prev = None
                self._head = self._head.next
            self._size -= 1
    
    def __iter__(self):
        ptr = self._head
        while ptr is not None:
            yield ptr.value
            ptr = ptr.next
    
    def __len__(self):
        return self._size


class _Entry:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


if __name__ == '__main__':
    q = Queue(5)

    for n in range(10):
        q.add(n)
        print('ADD', n, list(q))

    while len(q) > 0:
        print('REM', q.remove(), list(q))