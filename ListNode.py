class ListNode:
    def __init__(self,data):
        self.data=data
        self.next=None

    def printList(self,head):
        while head is not None:
            print(head.data,end=" ")
            head=head.next
        print()

    def reverseList(self,head):
        prev = None
        while head is not None:
            temp=head.next
            head.next=prev
            prev=head
            head=temp
        return prev

