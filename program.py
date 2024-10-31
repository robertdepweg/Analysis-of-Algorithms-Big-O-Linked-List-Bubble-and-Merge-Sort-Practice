"""Program code"""

# First-party imports
from datastructures import LinkedList, HashTable
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

    ###################
    # Hash table work #
    ###################

    # Demonstrate how the hash table works
    valley_num_to_name = HashTable()
    print()
    print("adding some entries to the HashTable")
    print("EX: valley_num_to_name.put(12345, 'David Barnes')")
    
    valley_num_to_name.put(12345, "James Kirk")
    valley_num_to_name.put(23453, "Charles Legend")
    valley_num_to_name.put(74023, "Kathryn Long")
    valley_num_to_name.put(94610, "Matthew Homes")
    valley_num_to_name.put(56435, "Jalyn Deo")

    print("The created hash table")
    print(valley_num_to_name)
    print(valley_num_to_name.show_array())
    print("************************")

    print("Get a single value out from the hash table")
    print("valley_num_to_name.get(45678)")
    print(valley_num_to_name.get(45678))
    print()

    print("What if we add 2 entries that collide?")
    print("valley_num_to_name.put(26189, 'First Entry')")
    print(valley_num_to_name.put(26189, 'First Entry'))
    print("valley_num_to_name.put(26092, 'Second Entry')")
    print(valley_num_to_name.put(26092, 'Second Entry'))
    
    print()
    print(valley_num_to_name)
    print(valley_num_to_name.show_array())
    print()

    print("Get the first entry out")
    print("valley_num_to_name.get(26189)")
    print(valley_num_to_name.get(26189))
    print("Got second entry instead. First was overwritten.")
    print()
    print()

    # What if we use string keys?
    print("What about using string keys?")
    string_hash_table = HashTable()
    string_hash_table.put("foobar", "Joe Smith")
    string_hash_table.put("barbaz", "Brenda Sams")
    print(string_hash_table.get("foobar"))
    print(string_hash_table.get("barbaz"))
    print(string_hash_table)
    print("String keys work too.")

