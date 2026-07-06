class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=None

head=None
tail=None
for j in range(1,11):
    new_node=Node(j*10)
    if head is None:
        head=new_node
        tail=new_node
    else:
        tail.next=new_node
        tail=new_node


current=head
while current:
    print(current.val)
    current=current.next
