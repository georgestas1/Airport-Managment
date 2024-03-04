
class Node:
    def __init__(self, data, priority) -> None:
        self.data = data  # data stored in the node
        self.priority = priority  # priority of the node
        self.next = None  # reference to the next node
        self.prev = None  # reference to the previous node

    def __str__(self):
        return str(self.data)
    

class PriorityQueue:
    def __init__(self) -> None:
        self.head = None  # reference to the head of the priority queue
        self.tail = None  # reference to the tail of the priority queue

    def insert(self, data, priority):
        node = Node(data, priority)  # create a new node
        if self.head is None:  # if the priority queue is empty
            self.head = node  # set the new node as the head
            self.tail = node  # set the new node as the tail
        else:
            iter = self.head  # start iterating from the head
            while iter is not None and iter.priority < priority:
                iter = iter.next  # move to the next node until priority is higher or end is reached
            if iter is None:  # if the new node has the highest priority
                self.tail.next = node  # set the new node as the next node of the current tail
                node.prev = self.tail  # set the current tail as the previous node of the new node
                self.tail = node  # set the new node as the new tail
            else:
                if iter == self.head:  # if the new node has the lowest priority
                    iter.prev = node  # set the new node as the previous node of the current head
                    node.next = iter  # set the current head as the next node of the new node
                    self.head = node  # set the new node as the new head
                else: 
                    iter.prev.next = node  # set the new node as the next node of the previous node of iter
                    node.prev = iter.prev  # set the previous node of iter as the previous node of the new node
                    iter.prev = node  # set the new node as the previous node of iter
                    node.next = iter  # set iter as the next node of the new node

    def empty(self):
        return self.head is None and self.tail is None  # check if the priority queue is empty

    def peek(self):
        # return the highest priority Node without removing
        if self.tail is None:  # if the priority queue is empty
            return None
        else:
            return self.tail  # return the tail node

    def remove(self):
        # remove and return the highest priority Node
        if self.tail is None:  # if the priority queue is empty
            return None
        elif self.tail == self.head:  # if there is only one node in the priority queue
            node = self.tail  # store the tail node
            self.tail = None  # set the tail to None
            self.head = None  # set the head to None
        else:
            node = self.tail  # store the tail node
            self.tail = self.tail.prev  # set the previous node of the tail as the new tail
            self.tail.next = None  # set the next node of the new tail to None
        return node  # return the removed node

    def traverse(self):
        # visit and print each node, just for testing
        iter = self.head  # start iterating from the head
        while iter is not None:
            print(iter)  # print the current node
            iter = iter.next  # move to the next node

    def change_priority(self, data, new_priority):
        pass  # TODO: Implement the change_priority method


if __name__ == "__main__":
    pq = PriorityQueue()
    pq.insert("Peter", 0)
    pq.insert("Ann", 0)
    pq.insert("Tom", 1)
    pq.insert("James", 0)
    pq.insert("Nick", 4)
    pq.insert("Alice", 1)
    pq.insert("Jim", 3)
    pq.traverse()
    node = pq.remove()
    print("Serve: ", node)
    pq.traverse()

    print("Peek: ", pq.peek())
