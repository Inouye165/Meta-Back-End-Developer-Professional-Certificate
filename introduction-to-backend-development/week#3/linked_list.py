class Node:
    """
    Represents a node in the linked list.
    """
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node

class LinkedList:
    """
    Represents the entire linked list.
    """
    def __init__(self):
        self.head = None  # The head of the list

    def append(self, data):
        """
        Adds a new node with the given data to the end of the list.
        """
        new_node = Node(data)

        # If the list is empty, the new node becomes the head
        if self.head is None:
            self.head = new_node
            return

        # Traverse to the last node
        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node  # Add the new node at the end

    def print_list(self):
        """
        Prints the data of each node in the list.
        """
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
my_list = LinkedList()
my_list.append(1)
my_list.append(5)
my_list.append(3)
my_list.print_list()  # Output: 1 -> 5 -> 3 -> None 
my_list.append(73)
my_list.print_list
