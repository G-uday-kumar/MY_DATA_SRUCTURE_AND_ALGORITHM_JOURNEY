class Node:
    def  __init__(self,val=0,next=None):
        self.val=val
        self.next=next
node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)
node5=Node(50)
node6=Node(60)
node7=Node(70)


head=node1
current=head
while current:
    print(current.val)
    current=current.next

