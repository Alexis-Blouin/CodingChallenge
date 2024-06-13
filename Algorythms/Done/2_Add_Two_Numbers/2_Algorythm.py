class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        value_1 = l1.val
        next_val_1 = l1.next
        num_1 = 0
        value_2 = l2.val
        next_val_2 = l2.next
        num_2 = 0
        i = 0
        while True:
            if next_val_1 is not None:
                num_1 += value_1 * 10**i
                value_1 = next_val_1.val
                next_val_1 = next_val_1.next
            elif value_1 != -1:
                num_1 += value_1 * 10**i
                value_1 = -1
            if next_val_2 is not None:
                num_2 += value_2 * 10**i
                value_2 = next_val_2.val
                next_val_2 = next_val_2.next
            elif value_2 != -1:
                num_2 += value_2 * 10**i
                value_2 = -1
            if value_1 == -1 and value_2 == -1:
                break
            i += 1

        sum = str(num_1 + num_2)
        l3 = ListNode()
        next_val = None
        for digit in sum:
            val = digit
            l3 = ListNode(val, next_val)
            next_val = l3
        return l3


if __name__ == "__main__":
    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    l3 = Solution().addTwoNumbers(l1, l2)
    result = []
    while l3 is not None:
        result.append(l3.val)
        l3 = l3.next
    print(result)
