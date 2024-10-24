"""Program code"""

# First-party imports
from datastructures import LinkedList
from employee import Employee


def main(*args):
    """Method to run program"""
    # Make instance of Linked List.
    linked_list = LinkedList()

    # Add to the front and back a few times.
    linked_list.add_to_front(5)
    linked_list.add_to_front(4)
    linked_list.add_to_front(3)
    linked_list.add_to_back(6)
    linked_list.add_to_back(7)
    linked_list.add_to_back(8)

    print("This list is:")
    print(linked_list)
    print()

    # Remove from Front
    linked_list.remove_from_front()
    linked_list.remove_from_front()
    linked_list.remove_from_front()

    print("This list is:")
    print(linked_list)
    print()

    # Remove from back a couple of times
    linked_list.remove_from_back()
    linked_list.remove_from_back()

    print("This list is:")
    print(linked_list)
    print()

    # Also have ability to get the value that was returned
    returned_number = linked_list.remove_from_back()

    print("The removed number is:")
    print(returned_number)

    # Can also use full on objects inside of it if needed.
    employee_list = LinkedList()
    employee_list.add_to_front(Employee("David", "Barnes", 750.00))
    employee_list.add_to_front(Employee("Jean-Luc", "Picard", 750.00))
    print(employee_list)
