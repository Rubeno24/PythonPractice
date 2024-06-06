from ListNode import ListNode

head = ListNode(1)
head.next = ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)

head.printList(head)

reversedList=head.reverseList(head)

reversedList.printList(reversedList)

