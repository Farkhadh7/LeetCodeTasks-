Picture two lines of people, each already sorted by height, and you need to merge them into one sorted line.

The idea: Look at the first person in each line. Whoever is shorter goes next in the new line. Then look at the two fronts again and repeat. Since both lines are already sorted, the shorter front person is always the correct next person overall.

The dummy node: Building a linked list has an annoying problem: the first node is special because you don't know yet which list it will come from. To avoid extra if checks, we create a fake starting node called dummy. We build the whole merged list after it, and at the end we return dummy.next, which is the real head.

The tail pointer: This always points to the last node of the merged list so far. To add a node, we set tail.next to it and move tail forward.

The loop: While both lists still have nodes:

Compare list1.val and list2.val.
Attach the smaller node to the merged list.
Move that list's pointer forward by one.
Move tail forward.

The leftovers: When one list runs out, the other one may still have nodes. Since they're already sorted and all bigger than what we've placed, we attach the whole remaining chain in one go with tail.next = list1 if list1 else list2. No more looping needed.

Walking through Example 1: list1 = [1,2,4], list2 = [1,3,4]

1 vs 1: take from list1 (we use <=), giving [1].
2 vs 1: take from list2, giving [1,1].
2 vs 3: take from list1, giving [1,1,2].
4 vs 3: take from list2, giving [1,1,2,3].
4 vs 4: take from list1, giving [1,1,2,3,4].
list1 is empty, so attach the leftover [4] from list2, giving [1,1,2,3,4,4]. ✅

Edge cases: If both lists are empty, the loop never runs, tail.next becomes None, and we return dummy.next, which is None (an empty list). ✅ If one list is empty, the other is attached entirely. ✅

Complexity:

Time: O(n + m), since each node is visited once.
Space: O(1), since we reuse the existing nodes and only add one dummy node.