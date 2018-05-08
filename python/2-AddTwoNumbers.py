# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from decimal import *

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 使用decimal类型，并指定位数
        getcontext().prec = 100
        n1 = self.listToNumber(l1)
        n2 = self.listToNumber(l2)
        n = n1+n2
        #print("{:f}+{:f}={:f}".format(n1,n2,n))
        return self.numberToList(n)

    def listToNumber(self, l):
        # 考虑大数相加，使用decimal类型数计算
        number = Decimal(0.0)
        i = 0
        while l != None:
            number += l.val * (10**i)
            i += 1
            l = l.next
        return number

    def numberToList(self, number):
        # 考虑大数会自动转换为科学计数法
        v = number % 10
        head = ListNode(int(v))
        p = head
        while number > 9:
            number = (number-v)/10
            v = number % 10
            p.next = ListNode(int(v))
            p = p.next
        return head

    def printList(self, l):
        while l != None:
            print(l.val, end="")
            l = l.next

    def readList(self, l):
        dummy = ListNode(0)
        p = dummy
        for x in l:
            p.next = ListNode(x)
            p = p.next
        return dummy.next

if __name__ == "__main__":
    # case 1
    l = Solution().readList([2,4,3])
    print(Solution().listToNumber(l))

    p = Solution().numberToList(465)
    print(Solution().listToNumber(p))

    print(Solution().printList(Solution().addTwoNumbers(l, p)))

    # case 2
    print(Solution().printList(Solution().numberToList(123.0)))

    # case 3
    l = Solution().readList([2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,9])
    p = Solution().readList([5,6,4,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,2,4,3,9,9,9,9])
    print(Solution().listToNumber(l))
    print(Solution().listToNumber(p))
    print(Solution().printList(Solution().addTwoNumbers(l, p)))
