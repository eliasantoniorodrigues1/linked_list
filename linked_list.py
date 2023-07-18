
class Node(object):
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

    def get_next(self):
        return self.nextNode
    
    def set_next(self, nextNode):
        self.nextNode = nextNode

    def get_data(self):
        return self.value
        

class LinkedList(object):
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def get_size(self):
        return self.size
    
    def add(self, value):
        new_node = Node(value, self.root)
        self.root = new_node
        self.size += 1

    def remove(self, value):
        this_node = self.root
        prev_node = None

        while this_node:
            if this_node.get_data() == value:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node
                self.size -= 1

                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
            
            return False
        
    def find(self, value):
        this_node = self.root
        while this_node:
            if this_node.get_data() == value:
                return value
            else:
                this_node = this_node.get_next()
        return None
    

if __name__ == '__main__':
    myList = LinkedList()
    myList.add(5)
    myList.add(8)
    myList.add(12)
    print(myList.remove(12))
    print(myList.find(5))
