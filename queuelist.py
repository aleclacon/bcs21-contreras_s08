'''
Queue
    same as stacks
    ADT - abstract data type
    FIFO - First IN First OUT
        the first element inserted into queue will be very first one processed
        data is inserted at the top (rear) and the data deletion is at the bottom(front)
    Rear Insertion: Bottom/ Front - Deletion
    Ex: Enrollment Line, Parking Lot
Operation of queue:
    Enqueue:
        inserts a new element at the top of a queue
    Dequeue:
    isEmpty
    isFull:
    isPeek:
'''
'''
Algorithm of Enqueue

Enqueue (head, tall, value)
{
    create a node
    address of new node -> node.data = value
    address of new node -> node.link = Null
    if(head <> NULL ) then
    {
    tall -> node.link=address of new node
    }else{
    head =address of new node
    }
    tail = address of new node 
    }
}
'''

class Node:
    def __init__(self,data= None):
        self.data = data 
        self.next = None
class Queue:
    def __init__(self,capacity):
        self.head = None
        self.tail = None
        self.capacity = None
        
    def enqueue(self,value):
        new_node = Node (value)

        if self.head is None:
            self.head =new_node
            self.tail = new_node
        else:
            self.tail.next =new_node
            self.tail= new_node
    def dequeue(self):
        current_node = self.head
        if self.head is None:
            return None
        else:
            removed_node = self.head
            self.head = self.head.next
            return removed_node.data
        
    def flow(self):
        if self.head is None:
            print("MESSAGE : Underflow. The Queue is empty.")
        else: 
            print("MESSAGE : Overflow. The queue is full.")

    def print_queue(self):
        current_node = self.head
        while current_node:
            print(f"current_node.data, next: {hex(id(current_node.next))}")
            current_node = current_node.next
        print()


queue = Queue(5)

queue.flow()
queue.enqueue('Monday')
queue.enqueue('Tuesday')
queue.enqueue('Wednesday')
queue.enqueue('Thursday')
queue.enqueue('Friday')
queue.enqueue('Saturday')
queue.enqueue('Sunday')
queue.print_queue()
queue.flow()

print(f'Dequeued: ({queue.dequeue()})')
print(f'Dequeued: ({queue.dequeue()})')
print(f'Dequeued: ({queue.dequeue()})')
print(f'Dequeued: ({queue.dequeue()})')
print(f'Dequeued: ({queue.dequeue()})')
print(f'Dequeued: ({queue.dequeue()})')
print(f'Dequeued: ({queue.dequeue()})')
print(f'Dequeued: ({queue.dequeue()})')
queue.flow()
queue.print_queue()






'''
dequeue(head, tail)
{
    if head <> Null then
    {
        node.delete = head
        print head -> node.data
        if head =null
        {
        tail =null
        }else{
            print "Underflow or Empty List"
        }
        free (node_delete)
        }
    }
}
 eme
queue.flow()
print(f'Dequeued: ({queue.dequeue()})')
queue.print_queue()


queue.flow()
print(f'Dequeued: ({queue.dequeue()})')
queue.print_queue()


queue.flow()
print(f'Dequeued: ({queue.dequeue()})')
queue.print_queue()

eme

Mini-activity

Enhance the sample code by adding the "Underflow" and "Overflow" in list 
screenshot the sample solution and the result
'''