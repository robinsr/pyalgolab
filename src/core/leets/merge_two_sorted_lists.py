from helpers.list_node import ListNode

# Q:
#  You are given the heads of two sorted linked lists list1 and list2. Merge the two lists into
#  one sorted list. The list should be made by splicing together the nodes of the first two lists.
#
# Constraints:
#   • The number of nodes in both lists is in the range [0, 50].
#   • -100 ≤ Node.val ≤ 100
#   • Both list1 and list2 are sorted in non-decreasing order.


def merge_two_sorted_lists(la: ListNode, lb: ListNode) -> [int]:
    slist = []

    while la is not None and lb is not None:
        if la.val < lb.val:
            slist.append(la.val)
            la = la.next
        else:
            slist.append(lb.val)
            lb = lb.next

    # Reached the end of one list, add remaining items from other list
    while la is not None:
        slist.append(la.val)
        la = la.next

    while lb is not None:
        slist.append(lb.val)
        lb = lb.next

    return slist