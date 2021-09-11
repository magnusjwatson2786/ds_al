class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next_node=None 

    def __repr__(self) -> str:
        return f"<Node, data: {self.data}>"

class LinkedList:
    def __init__(self) -> None:
        self.head=None

    def __repr__(self) -> str:
        curr=self.head
        nodes=[]
        while curr:
            nodes.append(str(curr).split(": ")[1].strip(">"))
            curr=curr.next_node
        return "Head :"+ "]->".join(nodes) +": Tail"

    def isEmpty(self)-> bool:
        return self.head==None

    def size(self)->int:
        curr=self.head
        c=0
        while curr:
            c+=1
            curr=curr.next_node
        return c

    def add(self,data)->None:
        new=Node(data)
        new.next_node=self.head
        self.head=new

    def search(self,key):
        curr=self.head
        while curr:
            if curr.data==key:
                return curr
            else:
                curr=curr.next_node
        return None

    def insert(self,data,index:int=0)->None:
        if not index:
            self.add(data)

        if index>0:
            new=Node(data)
            pos=index
            curr=self.head
            while pos>1:
                curr=curr.next_node
                pos-=1
            next=curr.next_node

            curr.next_node=new
            new.next_node=next

    def remove(self,key)->None:
        curr=self.head
        prev=None

        while curr:
            if curr.data ==key and curr is self.head:
                self.head=curr.next_node
                break
            if curr.data==key:
                prev.next_node=curr.next_node
                break
            prev=curr
            curr=curr.next_node
        
        # return curr