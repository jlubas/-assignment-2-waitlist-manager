# Create a Node class to represent each customer in the waitlist
class Node:
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''
    def __init__(self, name):
      self.name = name
      self.next = None


# Create a LinkedList class to manage the waitlist
class LinkedList:
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    Methods:
        add_front(name): Adds a customer to the front of the waitlist.
        add_end(name): Adds a customer to the end of the waitlist.
        remove(name): Removes a customer from the waitlist by name.
        print_list(): Prints the current waitlist.
    '''
    
    def __init__(self):
        self.head = None

    def add_front(self, name):
       new_node = Node(name)
       new_node.next = self.head
       self.head = new_node

    def print_list(self):
        if self.head is None:
            print("The waitlist is empty")
            return

        print("Current waitlist:")
        current = self.head

        while current is not None:
            print(f"- {current.name}")
            current = current.next
    def add_end(self, name):
            new_node = Node(name)

            if self.head is None:
              self.head = new_node
            else:
              current = self.head

              while current.next is not None:
                   current = current.next
              current.next = new_node

            return f"{name} added to the end of the waitlist"   

    def remove(self, name):
          if self.head is None:
              return f"{name} not found"

          if self.head.name == name:
             self.head = self.head.next
             return f"Removed {name} from the waitlist"

          current = self.head

          while current.next is not None:
            if current.next.name == name:
               current.next = current.next.next
               return f"Removed {name} from the waitlist"

            current = current.next

          return f"{name} not found"

def waitlist_generator():
    # Create a new linked list instance

    waitlist = LinkedList()
    
    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")
        
        choice = input("Choose an option (1–5): ")
        
        if choice == "1":
            name = input("Enter customer name to add to front: ")
            # Call the add_front method
            waitlist.add_front(name)

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            # Call the add_end method
            waitlist.add_end(name)

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            # Call the remove method
            result = waitlist.remove(name)
            if result == f"{name} not found":
                print(result)

        elif choice == "4":
        
            # Print out the entire linked list using the print_list method.
            waitlist.print_list()
            
        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid option. Please choose 1–5.")
5
# Call the waitlist_generator function to start the program

waitlist_generator()

'''
Design Memo: Write Your Design Memo Include a 200–300 word response in your code or in a .txt file:
- How does your list work?
My linked list is like a line of people waiting. Each person is stored in a Node. 
The Node keeps the person’s name and also knows who comes next in line. If I add someone to the front, they become the first person. 
If I add someone to the end, the program starts at the first person and keeps moving to the next person until it finds the end. 
If I remove someone, the program finds that person and connects the people before and after them so the line still stays together.

- What role does the head play?
The head is like a sign that points to the first person in line. The program uses the head to know where the list starts. 
If no one is in the waitlist, the head is None. If someone new is added to the front, the head changes to that person.
If the first person leaves, the head moves to the next person.
 
- When might a real engineer need a custom list like this?
A real engineer could use a list like this when people or items are always being added and removed. 
A waitlist is a good example because people can join or leave at different times. 
This project helped me understand that a linked list is made of Nodes that are connected together, and the head and next pointers help the program know where the list starts and where each person goes next.
'''
