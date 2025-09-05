class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"ListNode(val={self.val}, next={self.next})"


def build_list(xs):
    head = curr = ListNode(0)  # dummy
    for x in xs:
        curr.next = ListNode(x)
        curr = curr.next
    return head.next


def to_list(node):
    out = []
    while node and node.val:
        out.append(node.val)
        node = node.next
    return out