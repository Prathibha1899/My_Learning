## Maximum Product of Two Elements in an Array
**Aim**: Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).<br>

**Solution 1**:
~~~python
from typing import List
nums = [1,5,4,5]
def maxProduct(nums: List[int]) -> int:
    length = len(nums)
    max_prod = 0
    max_indices = (0, 0)
    for i in range(length):
        current_val = nums[i]
        j = i + 1
        while j < length:          
            next_val = nums[j]
            prod = current_val * next_val
            if prod > max_prod:
                max_vals = (nums[i], nums[j])
                max_prod = prod
            j += 1
    i, j = max_vals      
    max_prod = (i-1) * (j-1)    
    return max_prod
            
maxProduct(nums)
~~~
**Output is 16**
## Question 1:
**How does the first solution with two loops tackle the problem? What is it is time and space complexity and how do you know this?** <br>
**Ans:**<br>
**Code Explanation :**<br>
The outer loop of the above code iterates over each element in the array using the index i. For every outer loop, the inner loop starts from the next element (j = i + 1) and iterates to the end of the array. 'current_val' stores the value of index i and 'next_val' stores value of index j. product of current_val and next_val is stored in 'prod'. variable 'max_prod' is initialised outside the loops to 0 and compared with the 'prod' for every inner loop. if 'prod' is greater than 'max_prod' then 'max_vals' stores the values of the indices i and j and 'max_prod' is updated to 'prod'. This check happens for the every inner loop of the outer loop. after the for loop ends, we get the values which give max product from 'max_vals' and then we return the result which is (i-1)*(j-1).<br>

**Time Complexity** <br>
The solution uses nested loop to go through all the elements in the array. outer loop runs for n times where n is the length of the array. Inner loops runs for n-1 times for each iteration of outer loop. so on the total it takes n*(n-1) iterations. Therefore, it's time complexity is **O(n^2)**.<br>

**Space Complexity**:<br>
Space Complexity is **O(1)** because the code uses only constant amount of space. All the variables use constant space.<br>

I can come to this conclusion because the code goes through every possible pair of the elements in the array and compares it with maximum product. <br>

**Solution 2**:
~~~python
def maxProduct(nums: List[int]) -> int:
    nums.sort() # n log n
    length = len(nums)
    return (nums[length-1]-1) * (nums[length-2]-1)
maxProduct(nums) 
~~~

## Question 2:
**How does the second solution using sorting work? What is the time and space complexity and how do you know this?**<br>
**Ans:**<br>
**Code Explanation :**<br>
The second solution sorts the array first. After sorting the largest element is at index (length-1) and second largest is at index (length-2). product of these elements after subtracting 1 gives the required maximum product.<br>

**Time Complexity**:<br>
The sorting in the code takes O(n*log n) because any built in sort takes O(n*log n) complexity. Finding largest elements takes O(1) as the indexing takes constant time. Over all it takes O(n*log n).<br>

**Space Complexity**:<br>
Sort function sorts the elements in the place so it doesn't take any extra space. Therefore it takes O(1) space.<br>

I can come to this conclusion because the code uses sort in the code.<br>

This code is efficient than the first solution as O(n*log n ) is better than O(n^2). But the problem here is it doesn't work as expected when the array consists negative elements. So it might not be the better solution for the negative cases.<br>

**Solution 3**:
~~~python
nums = [10,2,5,2]
def maxProduct(nums: List[int]) -> int:
    max_val = 0
    max_val_1 = 0
    for val in nums:
        if val >= max_val:
            max_val_1 = max_val
            max_val = val
            print(max_val, max_val_1)
        elif val > max_val_1:
            max_val_1 = val
            
    return (max_val-1) * (max_val_1-1)
    
maxProduct(nums)   
~~~

## Question 3:
**How does the third solution work? How can you modify it to handle the case for two large negative numbers?  What is the time and space complexity and how do you know this? What is the main trick or insight that you learned from the final solution? HINT: How are you storing two max or two min values in just one loop.** <br>
**Ans:**<br>
**Code Explanation :**<br>
The code iterates through each element 'val' in the array 'nums'. if the 'val' is greater than 'max_val' is is intialised to 0 then the 'max_val' is updated to the 'val' and 'max_val_1' which stores the second largest stores the 'max_val'. If 'val' is greater than 'max_val_1' but less than 'max_val', 'max_val_1' is updated to 'val'. after the loop ends, the function returns the product of (max_val-1)  and (max_val_1-1).<br>

This code is an efficient one when compared to the other solutions as it iterates through array just one time. But the code doesn't handle the negative numbers case. so the  code has to be slightly modified to handle the large negative numbers. Below is the modified code.<br>

**Modified Code**:
~~~python
nums = [-100,-99,3,4]
def maxProduct(nums: List[int]) -> int:
    max_val = float('-inf')
    max_val_1 = float('-inf')
    min_val = float('inf')
    min_val_1 = float('inf')
    for val in nums:
        if val > max_val:
            max_val_1 = max_val
            max_val = val
        elif val > max_val_1:
            max_val_1 = val
            
        if val < min_val:
            min_val_1 = min_val
            min_val = val
        elif val < min_val_1:
            min_val_1 = val
        
    max_res = (max_val-1) * (max_val_1-1)
    min_res = (min_val-1) * (min_val_1-1)

    return max(max_res, min_res)
    
maxProduct(nums)  
~~~
The above code is similar to the previous one but the change here is we are also calculating smallest and second smallest  numbers along with the largest and second largest  numbers. This is important because the product of two negative numbers can be positive and could be larger than the product of two positive numbers in certain cases. max_val and max_val_1 are initialized to negative infinity (float('-inf')). These variables will store the two largest values found in the array. min_val and min_val_1 are initialized to positive infinity (float('inf')). These variables will store the two smallest values found in the list. Rest of the code is similar to the previous code. After finding the required largest and smallest numbers. their product is compared using max in-built function to get the maximum product.<br>

**Time Complexity**:<br>
The code iterates through the array once, that is n times, so it takes linear time .i.e **O(n)** .<br>

**Space Complexity**:<br>
Space Complexity is **O(1)** because the code uses only constant amount of space. All the variables use constant space.<br>

I can come to this conclusion because the code iterates through the array just once.<br>

**Insights**:<br>
The key insight here is we can just use single loop to get the two largest values of a given array and two smallest values as well. This can be achieved by Comparing each element in the array with max_val and max_val_1 to update the two largest values. Similarly, comparing each element with min_val and min_val_1 to update the two smallest values.

## Find All Duplicates in an Array
**Aim**: Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.<br>

You must write an algorithm that runs in O(n) time and uses only constant extra space.<br>
**Solution 1**:
~~~python
lst = [1, 3, 1, 3, 5, 1, 4, 7, 7]
def find_duplicates(lst):
    counter = {}
    for val in lst:
        if val not in counter:
            counter[val] = 0
        counter[val] += 1 
    result = []
    for val, count in counter.items():
        if count > 1:
            result.append(val)
    return result

find_duplicates(lst)
~~~

**Question 1**:<br>
**How does the first solution using set and dictionary work? What is it is time and space complexity and how do you know this? Also, does it meet the criteria set by the problem?**<br>
**Ans:**<br>
**Code Explanation :**<br>
The above code uses a dictionary to count the occurances of the each element of the given array. Here, an empty dictionary counter is initialised to  store the count of each element. loop iterates through each element and if value is not already in counter it adds it to the counter dictionary with an initial count of 0 and then it increments the count by 1. If it is already present then it just increments the count by 1. after the loop ends , it goes through the every key and value of the counter and checks if any value is greater than 1 (checks if it is duplicate). If the 'count' which is value of each key is greater than 1, it is appended to the list 'result' which is intialised to an empty one before the checks. Finally it returns the 'result' list.<br>

**Time Complexity**:<br>
Code takes O(n) time  complexity this is beacuse Iterating through the list to count occurrences takes O(n) time. Iterating through the dictionary takes O(n) time in the worst case (if all elements are unique). Over all it takes O(n) time complexity.<br>

**Space Complexity**:<br>
The dictionary counter can store up to n unique elements, each with a count and result list can store n/2 elements. Therefore we require O(n) space.<br>

I can come to this conclusion because the code iterates through the array just once and using dictionary to store the count of occurances.<br>

The problem requires an algorithm that runs in O(n) time and uses only constant extra space. But the solution is using O(n) space and this doesn't satisfy the requirements of the question.<br>

**Solution 2**:<br>
~~~python
lst = [1, 3, 1, 3, 5, 1, 4, 7, 7]
def find_duplicates(lst):
    result = []
    seen = set()
    
    for val in lst:
        if val not in seen:
            seen.add(val)
        else:
            result.append(val)
            
    return result
find_duplicates(lst)
~~~
## Question 2:
**How does the second solution work using a list to mark things as seen?  What is it is time and space complexity and how do you know this?** <br>
The second solution uses a set to keep track of elements that have already been seen while iterating through the list. An empty list 'result' is initialised to store the duplicates and an empty set 'seen' to keep track of elements that have been encountered. the loop iterates through each element 'val' in lst and if val is not present in seen, it is added to the seen set and if it is already present the val is appended to the result list. After the loop ends, the function returns the result list.<br>

**Time Complexity**:<br>
The code runs in O(n) time, where n is the length of the input list. This is because Iterating through the list takes O(n) time. searching in a list takes constant time. Thus, it takes O(n) time.<br>

**Space Complexity**: <br>
The set seen can store up to n unique elements in the worst case.The list result can store up to n/2 elements in the worst case. Thus, the overall space complexity is O(n)<br>

Even this code doesn't meet the requirement of O(1) space complexity.

**Solution 3**:
~~~python
lst = [4,3,2,7,8,2,3,1]
def find_duplicates(lst):
    result = []
    for ele in lst:
        if lst[abs(ele) - 1] < 0:
            result.append(abs(ele))
        else:        
            lst[abs(ele)-1] *= -1
            print(ele, lst)
            
    return result
find_duplicates(lst)
~~~
## Question 3:
**how the list solution works by stepping through array one step at a time?**<br>
In this solution we don't use any dict/set to avoid the O(n) space complexity and we just go through the list and get the duplicates. Code works as below<br>

<img src="Image_1.JPEG" alt="Sample Image" width="800"/>
<img src="Image_2.JPEG" alt="Sample Image" width="800"/>
<img src="Image_3.JPEG" alt="Sample Image" width="800"/>



























