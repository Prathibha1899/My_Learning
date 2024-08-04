## Top K Elements
**Problem statement**:<br>  
To find top k elements in the given array<br>

**Example:**<br>
nums = [11, 15, 29, 2, 3, 16]<br>
K = 3<br>
Output:[15, 29, 16]<br>

**Solution**:<br>
~~~python
nums = [11, 15, 29, 2, 3, 16]
K = 3

import heapq
def top_k_numbers(nums, k):
    min_heap = []
    
    for i in range(k):
        heapq.heappush(min_heap, nums[i])
        
    for i in range(k, len(nums)):
        number = nums[i] 
        if number > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, number)
            
    return min_heap
    
top_k_numbers(nums, 3)
~~~

**Question 1**:<br>
**Explain why you load up k elements into a heap, which heap, min or max?**<br>
To solve the problem of finding the top K elements in an array, we first load the first K elements into a min-heap. A min-heap is a binary tree where the parent node is always smaller than or equal to its child nodes. By using a min-heap, we can efficiently keep track of the largest K elements. The key idea is that the smallest element in the heap is always at the root (min-heap property), which allows us to compare and potentially replace it with larger elements from the rest of the array. By pushing the first K elements into the min-heap, we create a baseline of the largest K elements found so far. Then, as we iterate through the rest of the array, we only add an element to the heap if it is larger than the smallest element currently in the heap, ensuring that the heap always contains the top K largest elements.<br>


**Question 2**:<br>
**How do you update the heap for k-N elements and why do you do that?**<br>
After loading the first K elements into the min-heap, we update the heap for the remaining elements in the array (from the K+1th element to the end). For each of these elements, we check if it is larger than the smallest element in the heap (the root of the min-heap). If it is, we remove the smallest element (using heapq.heappop) and add the new, larger element (using heapq.heappush). This process ensures that the heap always contains the largest K elements seen so far. By continually replacing the smallest element in the heap with larger elements from the array, we maintain a collection of the top K elements efficiently.

**Question 3**:<br>
**Essentially, how does a heap help you solve this problem?**<br>
A heap helps solve the problem of finding the top K elements by providing an efficient way to keep track of the largest K elements as we iterate through the array. Specifically, a min-heap allows us to always know the smallest of these K elements, which means we can quickly compare and replace it when we find a larger element in the array. By maintaining the min-heap, we ensure that it contains exactly the K largest elements at any given time, with the smallest of these K elements at the root. This approach is more efficient than sorting the entire array, especially for large arrays, as it limits the number of comparisons and replacements needed to maintain the top K elements. Alternatively, a max-heap can be used to solve the problem of finding the smallest K elements by keeping track of the largest element among these K elements. This way, if a smaller element is found in the array, it can replace the largest element in the heap, maintaining a collection of the smallest K elements. In both cases, heaps help manage and update the set of K elements efficiently.<br>


### Visual Representation
python
Input : nums = [11, 15, 29, 2, 3, 16], K = 3

# First For loop itertation :

Step 1: Heap: [11]

   11

Step 2: Heap: [11, 15]

     11
       \
        15
    
Step 3: Heap: [11, 15, 29]

     11
    /  \
   15   29



### Second for loop:

# Adding 2
Heap: [11, 15, 29]

     11
    /  \
   15   29


#Adding 3
Heap: [11, 15, 29]

     11
    / \
   15  29

#Adding 16 - Replaces 15 from the heap 
Heap: [11, 29, 15]  - [29, 15, 16]

     15
    /  \
   16   29
