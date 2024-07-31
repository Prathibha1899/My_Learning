**Sliding Window Median**<br>
**Problem statement**:<br>  
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle values.<br>

For examples, if arr = [2,3,4], the median is 3.<br>
For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.<br>
You are given an integer array nums and an integer k. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.<br>

Return the median array for each window in the original array. Answers within 10-5 of the actual value will be accepted.<br>

**Example 1:**<br>

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3<br>
Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]<br>
Explanation: <br>
Window position                Median<br>
---------------                -----<br>
[1  3  -1] -3  5  3  6  7        1<br>
 1 [3  -1  -3] 5  3  6  7       -1<br>
 1  3 [-1  -3  5] 3  6  7       -1<br>
 1  3  -1 [-3  5  3] 6  7        3<br>
 1  3  -1  -3 [5  3  6] 7        5<br>
 1  3  -1  -3  5 [3  6  7]       6<br>

**Solution:**
~~~python
class Solution:
    import heapq
    
    def __init__(self):  
        self.min_heap = []
        self.max_heap = []
        self.result = []

    def balanceHeaps(self):
        if len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        elif len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        


    def removeIndex(self, heap, removeNumber):
        idx = heap.index(removeNumber)
        last_node = heap[-1] 
        heap[idx] = last_node       
        del heap[-1]
        if idx < len(heap):
            if last_node > removeNumber:
                heapq._siftup(heap, idx)
            else:
                heapq._siftdown(heap, 0, idx)
        self.balanceHeaps()   


    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        for ind, num in enumerate(nums):
            # Insert
            if not self.max_heap or num <= -self.max_heap[0]:
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)

            self.balanceHeaps()
            
            if (ind+1) - k >= 0:
                if len(self.max_heap) == len(self.min_heap):
                    self.result.append((-self.max_heap[0] + self.min_heap[0]) / 2)
                else:
                    self.result.append(-self.max_heap[0] / 1.0)

                removeNumber = nums[ind+1-k]
                if removeNumber <= -self.max_heap[0]:
                    self.removeIndex(self.max_heap, -removeNumber)
                else:
                    self.removeIndex(self.min_heap, removeNumber)
                                                 
        return self.result
~~~

**Question 1**:<br>
 **Explain why you need a max and min heap and what kind of information they store.**<br>
To efficiently find the median of a sliding window in an array, we use two heaps: a max heap and a min heap. The max heap stores the smaller half of the numbers in the window, while the min heap stores the larger half. The max heap's root (the largest of the smaller half) helps us quickly find the median when the window size is odd. The min heap's root (the smallest of the larger half) helps when the window size is even, allowing us to calculate the median as the average of the two middle values. This setup allows us to easily add new numbers, remove old numbers, and find the median quickly as the window slides across the array.<br>

**Question 2**:<br>
**Explain that Python heap is a min heap and how that affects how you use it, hint negative**<br>
In Python, the heapq module provides a min heap by default, which means it always keeps the smallest element at the root. However, for the sliding window median problem, we also need a max heap to store the smaller half of the numbers. Since Python doesn't have a built-in max heap, we simulate one by inserting the negative of each number into the min heap. This way, the smallest element in the min heap (which is actually the negative of the largest number) effectively represents the largest element of the smaller half. When we need to access the largest number, we simply take the negative of the root of this heap. This trick allows us to efficiently manage both halves of the sliding window using Python's min heap.<br>

**Question 3**:<br>
**Explain why you need balance**<br>
We need to balance the two heaps to ensure we can quickly find the median. The max heap (storing the smaller half of the numbers) and the min heap (storing the larger half) must be kept balanced so that their sizes are either equal or the max heap has just one extra element. This balance is crucial because it allows us to determine the median efficiently: if the total number of elements is odd, the root of the max heap gives the median; if even, the median is the average of the roots of both heaps. Balancing the heaps ensures that we can always access the median in constant time, making the sliding window median calculation fast and efficient.<br>

**Question 4**:<br>
**Explain what the removeindex function does, hint it must maintain the heap condition, but how is that achieved**<br>
The removeIndex function is designed to remove a specific number from a heap while maintaining the heap's properties. When a number needs to be removed, the function first finds the index of this number in the heap. It then replaces this number with the last element in the heap and removes the last element. After this replacement, the heap might not satisfy the heap condition (where the parent node is always smaller or larger than its child nodes, depending on whether it's a min heap or max heap). To restore the heap condition, the function uses two operations: heapq._siftup and heapq._siftdown, which rearrange the elements to ensure the heap properties are maintained. This way, even after removing an element, the heap remains correctly structured, allowing efficient future operations.<br>
