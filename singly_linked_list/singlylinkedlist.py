class Node:
    def __init__(self,info,next=None):
        self.data = info
        self.next = next

class Singly_linked_list:
    def __init__(self,head= None):
        self.head= head

    def insertAtend(self,value):
        temp = Node(value)
        
        if(self.head !=None):
            t1 = self.head
            
            while(t1.next !=None):
                t1= t1.next
            t1.next=temp
        
        else:
            self.head =temp

    def insertAtBeg(self,value):
        temp=Node(value)
        temp.next=self.head
        self.head=temp
    
    def insertAtMid(self, value, after_value):
        temp = Node(value)
        if self.head is None:
            return False
        t1 = self.head
        while t1 is not None:
            if t1.data == after_value:
                temp.next = t1.next
                t1.next = temp
                return True
            t1 = t1.next
        return False

    def deleteLinkedlist(self,value):

        t1=self.head
        prev= t1
        if(t1.data == value):
            self.head=t1.next
            return True
        while(t1.next!=None):
            if(t1.data== value):
                prev.next = t1.next
                return True
                break
            else:
                prev=t1
                t1=t1.next 
                
        if(t1.data == value):
            prev.next = None        
    def printlinkedlist(self):
        elements=[]
        t1=self.head
        while(t1):
            print(t1.data,end=" ")
            elements.append(t1.data)
            t1=t1.next
        return elements
        print(t1.data,end=" ")

"""obj =Singly_linked_list()
obj.insertAtBeg(89)
obj.insertAtend(23)
obj.insertAtend(34)
obj.insertAtMid(78,23)
obj.insertAtMid(54,89)
print("\n ^ All singly linked list nodes",obj.printlinkedlist())
print("delete last element: 34",obj.deleteLinkedlist(34))
obj.printlinkedlist()
"""