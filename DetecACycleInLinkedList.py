"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

def has_cycle(head):
    if head is None:
    	return 0
    if head.next is None:
    	return 0
    #init two vars as head. Implementing Floyd's Cycle Check Algorithm
    
    h = head
    t = head

    while True:
    	if t.next is None:
    		return 0
    	else:
    		t = t.next

    	if h.next is None:
    		return 0
    	elif h.next.next is None:
    		return 0
    	else:
    		h = h.next.next

    	if h == t:
    		return 1

