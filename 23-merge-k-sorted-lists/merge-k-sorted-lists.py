import heapq

class Solution:
    def mergeKLists(self, lists):

        heap = []

        for i, node in enumerate(lists):
            if node != None:
                data = (node.val, i, node)
                heapq.heappush(heap, data)

        dummy = ListNode(0)
        current = dummy

        while len(heap) > 0:

            data = heapq.heappop(heap)

            value = data[0]
            index = data[1]
            node = data[2]

            current.next = node
            current = current.next

            if node.next != None:
                nextData = (node.next.val, index, node.next)
                heapq.heappush(heap, nextData)

        return dummy.next