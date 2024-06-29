class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def find_middle(head):
  slow = head
  fast = head.next

  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

  return slow

def merge(left, right):
  merged = tail = None
  while left and right:
    if left.data <= right.data:
      if not merged:
        merged = tail = left
      else:
        tail.next = left
        tail = tail.next
      left = left.next
    else:
      if not merged:
        merged = tail = right
      else:
        tail.next = right
        tail = tail.next
      right = right.next
  
  tail.next = left if left else right
  return merged

def mergeSort(head):
  """Sorts a linked list using Merge Sort."""
  if not head or not head.next:
    return head

  middle = find_middle(head)
  right = middle.next
  middle.next = None 

  left = mergeSort(head)
  right = mergeSort(right)

  return merge(left, right)


def print_list(head):
  while head:
    print(head.data, end=" -> ")
    head = head.next
  print("None")


head = Node(5)
head.next = Node(3)
head.next.next = Node(1)
head.next.next.next = Node(2)
head.next.next.next.next = Node(4)

print("Original List:")
print_list(head)

sorted_head = mergeSort(head)

print("\nSorted List:")
print_list(sorted_head)
print("Fadhil Erdya")