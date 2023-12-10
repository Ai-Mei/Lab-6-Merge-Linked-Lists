class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# Connect the two likend lists together.
def connect_linked_lists(list1, list2):
    current = list1
    while current.next is not None:
        current = current.next
    current.next = list2
    return list1  

# Sort the values of the linked list and return the proper order of the linked list.
def sort_linked_list(head):
    if not head or not head.next:
        return head
    tentative = ListNode(0)
    tentative.next = head
    current = head.next
    last_sorted = head
    while current:
        if current.value < last_sorted.value:
            last_sorted.next = current.next
            prev = tentative
            while prev.next and prev.next.value < current.value:
                prev = prev.next
            current.next = prev.next
            prev.next = current
            current = last_sorted.next
        else:
            last_sorted = current
            current = current.next
    return tentative.next

# Function that would convert the user input into a linked list.
def create_linked_list():
    while True:
        values = input("Enter values separated by spaces. Values should range between -100 to 100 only. The maximum input per list should be 50 values: ")
        values = [int(i) for i in values.split()]
        # Constraints:
        if 0 <= len(values) <= 50 and all(-100 <= val <= 100 for val in values):
            break
        else:
            print("Invalid input. Please make sure the number of entries is between 0 and 50, and values are between -100 and 100.")
    head = ListNode(values[0])
    current = head
    for i in values[1:]:
        current.next = ListNode(i)
        current = current.next
    return head


# Implementation:
list1 = create_linked_list()
list2 = create_linked_list()

connected_list = connect_linked_lists(list1, list2)
sorted_list = sort_linked_list(connected_list)

while sorted_list is not None:
    print(sorted_list.value, end=" ")
    sorted_list = sorted_list.next
