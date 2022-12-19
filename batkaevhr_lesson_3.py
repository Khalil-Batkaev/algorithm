class LinkedList:
    class _Node:
        def __init__(self, val):
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None

    def add_first(self, val):
        node = self._Node(val)
        if self.head:
            self.head.prev = node
            node.next = self.head
            self.head = node
        else:
            self.head = node
            self.tail = node

    def delete_first(self):
        if self.head and self.head.next:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.head = None
            self.tail = None

    def search(self, val):
        node = self.head
        pos = 1
        while node:
            if node.val == val:
                return pos
            pos += 1
            node = node.next
        return False

    def get_last(self):
        return self.tail

    def remove_last(self):
        if self.tail and self.tail.prev:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        else:
            self.head = None
            self.tail = None

    def add_last(self, val):
        node = self._Node(val)
        if self.tail:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node

    def sort(self):
        need_sort = True
        while need_sort:
            node = self.head
            need_sort = False
            while node and node.next:
                if node.val > node.next.val:
                    before = node.prev
                    after = node.next.next
                    current_node = node
                    next_node = node.next
                    current_node.next = after
                    current_node.prev = next_node
                    next_node.next = current_node
                    next_node.prev = before
                    if before:
                        before.next = next_node
                    else:
                        self.head = next_node
                    if after:
                        after.prev = current_node
                    else:
                        self.tail = current_node
                    need_sort = True
                node = node.next

    # Метод для разворота списка
    def revert(self):
        node = self.head
        # Меняем голову и хвост
        self.head, self.tail = self.tail, self.head
        # Меням указатели с предыдущего на следующий и наоборот
        while node:
            node.prev, node.next = node.next, node.prev
            node = node.prev

    def __str__(self):
        result = '['
        node = self.head
        while node:
            result += str(node.val)
            if node.next:
                result += ', '
            node = node.next
        result += ']'
        return result


if __name__ == '__main__':
    my_list = LinkedList()
    my_list.add_last(4)
    my_list.add_last(1)
    my_list.add_last(2)
    my_list.add_first(2)
    my_list.add_first(1)
    my_list.add_first(5)
    # my_list.delete_first()
    # my_list.remove_last()
    # print(my_list.search(4))
    print(my_list)
    # my_list.sort()
    # print(my_list)
    my_list.revert()
    print(my_list)
