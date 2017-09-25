class LinkedNode(object):
    def __init__(self, key = None, val = None, next = None):
        self.key = key;
        self.val = val;
        self.next = next;

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dict = dict();
        self.head = LinkedNode();
        self.tail = self.head;
        self.capacity = capacity
    
    def _front(self):
        del self.dict[self.head.next.key];
        self.head.next = self.head.next.next;
        self.dict[self.head.next.key] = self.head;
        return;
    
    def _back(self, node):
        self.dict[node.key] = self.tail;
        self.tail.next = node;
        self.tail = node;
        return;
    
    def _kick(self, prev):
        node = prev.next;
        if node == self.tail:
            return;
        prev.next = node.next;
        if node.next:
            self.dict[node.next.key] = prev;
            node.next = None;
        self._back(node);
        return;
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if not key in self.dict:
            return -1;
        self._kick(self.dict[key]);
        return self.dict[key].next.val;
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dict.keys():
            prev = self.dict[key];
            self._kick(self.dict[key]);
            self.dict[key].next.val = value;
        else:
            node = LinkedNode(key=key, val=value);
            self._back(node);
            if len(self.dict.keys())>self.capacity:
                self._front();
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)