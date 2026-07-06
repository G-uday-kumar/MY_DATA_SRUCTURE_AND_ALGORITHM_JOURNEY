class LinkedList:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=None

node1=LinkedList(10)
node2=LinkedList(20)
node3=LinkedList(30)
node1.next=node2
node2.next=node3
head=node1
print(head)
current=head

while current:
    print(current.val)
    current=current.next
