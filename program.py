"""Program code"""

# First-party imports
from datastructures import LinkedList


def main(*args):
    """Method to run program"""
    # Make instance of Linked List.
    linked_list = LinkedList()

    # Add to the front and back a few times.
    linked_list.add_to_front(5)
    linked_list.add_to_front(3)
    linked_list.add_to_front(1)
