class node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class linkedlist:
    def __init__(self):
        self.head=None
    def insert(self,data):
        newnode=node(data)
        if(self.head):
            current=self.head
            while(current.next):
                current=current.next
            current.next=newnode
        else:
            self.head=newnode
    def iterate_item(self):
        current_item=self.head
        while current_item:
            val=current_item.data
            current_item=current_item.next
            yield val
ll=linkedlist()
ll.insert(10)
ll.insert(20)
ll.insert("welcome")
ll.insert(23)
print("list:")
for val in ll.iterate_item():
    print(val)
