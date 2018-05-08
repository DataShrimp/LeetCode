// No. 92

public class ReverseLinkedList2 {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        if (head == null)
            return null;

        ListNode dummy = new ListNode(0);
        dummy.next = head;

        ListNode pre, start, then;
        pre = dummy;
        for(int i=0; i<m-1; i++)
            pre = pre.next;

        start = pre.next;
        then = start.next;
        for(int i=0; i<n-m; i++) {
            start.next = then.next;
            then.next = pre.next;
            pre.next = then;
            then = start.next;
        }

        return dummy.next;
    }

    public static void main(String args[]) {
        ListNode h = new ListNode(1);
        h.next = new ListNode(2);
        h.next.next = new ListNode(3);
        h.next.next.next = new ListNode(4);
    }
}
