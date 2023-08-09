class node:
    def __init__(self,data):
        self.data =data
        self.next = None
class CLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.next = None
    
    def insertatbegin(self,data):
        t = node(data)
        if self.head is None:
            self.head = t
            self.tail = t 
            self.tail.next = self.head 
        else:
            t.next = self.head
            self.tail.next = t
            self.head = t  
            
    def display(self):
        if self.head is None:
            print("Empty Circular LinkedList")
        else:
            temp = self.head
            print(temp.data, end="-->")
            while(temp.next!=self.head):
                temp = temp.next
                print(temp.data,end="-->")
            print(temp.next.data,end="")
            print()
            
l= CLL()
n1 = node(10)
l.head = n1
l.tail = n1
l.tail.next = l.head

n2 = node(20)
l.tail.next=n2
l.tail =n2
l.tail.next = l.head

n3 = node(30)
l.tail.next = n3
l.tail = n3
l.tail.next = l.head

l.insertatbegin(5)

l.display()