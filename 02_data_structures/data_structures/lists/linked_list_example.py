#!/usr/bin/env python3
"""linked_list_example.py - Implementation of a singly linked list data structure.

This module demonstrates:
- Node class representing individual elements
- LinkedList class managing the node chain
- Common operations: insert, find, delete, traverse

A singly linked list is a linear data structure where each element (node)
points to the next element. The list maintains a reference to the first node (head).

Time Complexities:
- Insert at head: O(1)
- Find: O(n)
- Delete at index: O(n)
- Traverse: O(n)
"""


class Node:
    """Represents a single node in a linked list.
    
    Each node contains:
    - val: The data stored in the node
    - next: Reference to the next node (None if last node)
    """
    
    def __init__(self, val):
        """Initialize a new node with data.
        
        Args:
            val: The value to store in this node
        """
        self.val = val
        self.next = None

    def get_data(self):
        """Return the data stored in this node.
        
        Returns:
            The value stored in this node
        """
        return self.val

    def set_data(self, val):
        """Update the data stored in this node.
        
        Args:
            val: The new value to store
        """
        self.val = val

    def get_next(self):
        """Return the next node in the list.
        
        Returns:
            Node: The next node, or None if this is the last node
        """
        return self.next

    def set_next(self, next):
        """Set the next node reference.
        
        Args:
            next (Node): The node to link as the next node
        """
        self.next = next


class LinkedList:
    """Singly linked list implementation.
    
    The list maintains a head pointer to the first node and tracks
    the total count of nodes for efficient size queries.
    
    Attributes:
        head (Node): The first node in the list (None if empty)
        count (int): Number of nodes in the list
    """
    
    def __init__(self, head=None):
        """Initialize an empty linked list or with a head node.
        
        Args:
            head (Node, optional): Initial head node. Defaults to None.
        """
        self.head = head
        self.count = 0

    def get_count(self):
        """Return the number of nodes in the list.
        
        Returns:
            int: The count of nodes
        """
        return self.count

    def insert(self, data):
        """Insert a new node at the beginning of the list.
        
        This operation is O(1) as it always inserts at the head.
        
        Args:
            data: The value to store in the new node
        """
        # Create a new node with the data
        new_node = Node(data)
        # Point new node to current head
        new_node.set_next(self.head)
        # Update head to new node
        self.head = new_node
        # Increment count
        self.count += 1

    def find(self, val):
        """Find the first node containing the specified value.
        
        Traverses the list linearly from head to find matching value.
        Time complexity: O(n)
        
        Args:
            val: The value to search for
            
        Returns:
            Node: The first node with matching value, or None if not found
        """
        item = self.head
        # Traverse the list
        while item is not None:
            if item.get_data() == val:
                return item  # Found the value
            else:
                item = item.get_next()  # Move to next node
        
        return None  # Value not found in list

    def deleteAt(self, idx):
        """Delete the node at the specified index.
        
        Args:
            idx (int): Zero-based index of node to delete
            
        Note:
            - Does nothing if index is out of bounds
            - Special case for deleting head (index 0)
            - Time complexity: O(n)
        """
        # Check if index is valid
        if idx > self.count - 1:
            return
        
        # Special case: deleting head node
        if idx == 0:
            self.head = self.head.get_next()
            self.count -= 1
        else:
            # Traverse to node before the one to delete
            tempIdx = 0
            node = self.head
            while tempIdx < idx - 1:
                node = node.get_next()
                tempIdx += 1
            # Skip over the node to delete
            node.set_next(node.get_next().get_next())
            self.count -= 1

    def dump_list(self):
        """Print all values in the list from head to tail.
        
        Traverses the entire list and prints each value.
        Useful for debugging and visualization.
        """
        temp_node = self.head
        
        while temp_node:
            print(temp_node.get_data())
            temp_node = temp_node.get_next()


# ===== Demo: Using the LinkedList =====

# Create a linked list and insert some items
# Note: Items are inserted at head, so list order is reversed
itemlist = LinkedList()
itemlist.insert(38)  # List: 38
itemlist.insert(49)  # List: 49 -> 38
itemlist.insert(13)  # List: 13 -> 49 -> 38
itemlist.insert(15)  # List: 15 -> 13 -> 49 -> 38

print("Initial list:")
itemlist.dump_list()

# Exercise the contents of the list
print("\nItem count:", itemlist.get_count())
print("Finding item 13:", itemlist.find(13))
print("Finding item 78:", itemlist.find(78))  # Not in list

# Delete an item at index 3
print("\nDeleting item at index 3:")
itemlist.deleteAt(3)
print("Item count:", itemlist.get_count())
print("Finding item 38:", itemlist.find(38))  # Should be None after deletion

print("\nFinal list:")
itemlist.dump_list()
