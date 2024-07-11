## Two Pointers
The two-pointer pattern is a strategy used in programming to efficiently process a sequence of elements, like an array or string, by using two different pointers or indices.<br>
**Pointer**: A pointer is a position marker that helps keep track of an element in the sequence.<br>
**Two** **Pointers**: Instead of using just one position marker, we use two markers that generally start from different ends of the sequence and move towards each other.<br>

**How it Works**:<br>
**Initialization**: One pointer (left) starts at the beginning of the sequence, and the other pointer (right) starts at the end.<br>
**Comparison**: Compare the elements at these two pointers.<br>
**Movement**: Depending on the problem, we move the pointers towards each other. Typically, we increase the left pointer and decrease the right pointer.<br>
**Condition Check**: Continue this process until the pointers meet or cross each other.<br>

**Example of Two pointers Technique**:<br>
**Checking if a String is a Palindrome**:<br>
A palindrome is a word or phrase that reads the same forwards and backwards, like "MADAM."<br>
**Initialize Pointers**: Set left at the start (index 0) and right at the end (last index) of the string.<br>
**Compare Characters**: Check if the character at left is the same as the character at right.<br>
**Move Pointers**: If they match, move left one step to the right and right one step to the left. And keep comparing and moving until left is greater than or equal to right.<br>
**Check Result**: If all pairs of characters match, the string is a palindrome. If any pair doesn't match, it's not a palindrome.<br>

**Example 1**:<br>
String: M A D A M<br>
Index:  0 1 2 3 4<br>

Step 1: Compare M (left) and M (right) -> Match<br>
Step 2: Move pointers -> left = 1, right = 3<br>
Step 3: Compare A (left) and A (right) -> Match<br>
Step 4: Move pointers -> left = 2, right = 2<br>
Step 5: Pointers meet -> All matches, so "MADAM" is a palindrome.<br>

**Example 2**:<br>
String: ( ) ( )<br>
Index:  0 1 2 3<br>

Step 1: Compare ( (left) and ) (right) -> No match<br>
Step 2: Stop -> "()" is not a palindrome.<br>

**Example 2**:<br>
String: ) ( ( )<br>
Index:  0 1 2 3<br>

Step 1: Compare ) (left) and ( (right) -> No match<br>
Step 2: Stop -> ")()(" is not a palindrome.<br>

## Two Sum
**Problem statement**:Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target. Each input has exactly one solution. You may not use the same element twice. The order of the indices does not matter.<br>

**Example**:<br>
Input: nums = [2, 7, 11, 15], target = 9<br>
Output: [0, 1]<br>
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].<br>

**Solution**:<br>
~~~python
def two_sum(nums, target):
    indexed_nums = [(num, index) for index, num in enumerate(nums)]
    indexed_nums.sort()
    N = len(indexed_nums)
    left_index = 0
    right_index = N - 1
    while left_index < right_index:
        left_val, left_original_index = indexed_nums[left_index]
        right_val, right_original_index = indexed_nums[right_index]
        total = left_val + right_val
        if total == target:
            return [left_original_index, right_original_index]
        elif total > target:
            right_index -= 1
        else:
            left_index += 1

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))
output:[0,1]
~~~

**Explaination**:<br>
Firstly, we create a list of tuples, where each tuple contains a number and its original index. Then we sort the list of tuples. **The two-pointer approach assumes the array is sorted. If the array is not sorted, we need to sort it first. This is crucial because, in a sorted array, we can easily adjust the pointers to either increase or decrease the sum. A sorted array ensures that we can find the two numbers efficiently without having to check every possible pair.** Then we Initialize two pointers, one is  left_index at the beginning of the list and right_index at the end. we iterate the loop till the left_index is less then right_index. In the loop, firstly, we get the values and indices of the left and right pointer, then we sum them and store in 'total' variable. Now, we check if the total equals the target, if it is same we return the indices, if it is greater than the target value, we move the right pointer towards center by decreasing it by 1, if the target vale is less than the total, we move left pointer by increasing it by 1. By this at one point when we have the values 2 and 7, total gets equal to the total and it returns the indices 0 and 1.<br>

**Time Complexity**:<br>
The initial sorting of the array takes O(n log n). Once sorted, the two-pointer traversal takes O(n) since each pointer moves at most n times. Therefore, the overall time complexity is O(n log n), dominated by the sorting step. <br>

**Main Trick**:<br>
The main trick is leveraging the sorted nature of the array to efficiently adjust the pointers to find valid two indices without redundant checks, thus reducing the problem complexity compared to a naive two-loop approach, which would lead to a N^2 solution.<br>

## Three sum:
**Problem Statemnet**: Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == target.<br>

Notice that the solution set must not contain duplicate triplets.<br>

Example 1:<br>
Input: nums = [-1,0,1,2,-1,-4]<br>
target=0<br>
Output: [[-1,-1,2],[-1,0,1]]<br>
Explanation: <br>
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.<br>
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.<br>
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.<br>
The distinct triplets are [-1,0,1] and [-1,-1,2].<br>
Notice that the order of the output and the order of the triplets does not matter.<br>


**Solution**:
~~~python
def threeSum(nums, target):
    combinations = []
    nums.sort()  # O(N log N)

    N = len(nums)
    for i in range(0, N-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue  # skip duplicate elements to avoid duplicate triplets
        left_p = i + 1
        right_p = N - 1

        while left_p < right_p:
            x, y, z = nums[i], nums[left_p], nums[right_p]
            triplet = x + y + z

            if triplet == target:
                combinations.append([x, y, z])
                while left_p < right_p and nums[left_p] == nums[left_p + 1]:
                    left_p += 1  # skip duplicate elements
                while left_p < right_p and nums[right_p] == nums[right_p - 1]:
                    right_p -= 1  # skip duplicate elements
                left_p += 1
                right_p -= 1
            elif triplet < target:
                left_p += 1
            else:
                right_p -= 1
    return combinations

nums = [-1, 0, 1, 2, -1, -4]
target = 0
print(threeSum(nums, target))
Output: [[-1,-1,2],[-1,0,1]]
~~~

**Explanation**:
**Sort the Array**: The array is sorted to use the two-pointer technique effectively.<br>
**Fix One Element**: Use a for loop to fix one element (nums[i]).<br>
**Initialize Two Pointers**: Set left_p to i + 1 and right_p to the end of the array.<br>
**Check for Triplets**:<br>
Calculate the sum of the fixed element and the two-pointer elements.<br>
If the sum equals the target, add the triplet to the result list and skip duplicates.<br>
If the sum is less than the target, increment the left_p pointer by 1 to increase the sum.<br>
If the sum is greater than the target, decrement the right_p pointer by 1 to decrease the sum.<br>
**Avoid Duplicates**: Skip duplicate elements while fixing the element and adjusting the pointers to ensure unique triplets.<br>

**Time Complexity**:<br>
O(n log n) for sorting and O(n²) for the pointer approach because the two-pointer approach is applied for each element. The overall time complexity is O(n²), making this approach efficient for the 3Sum problem.<br>

**Main Trick**:<br>
The main trick is leveraging the sorted nature of the array to efficiently adjust the pointers to find valid triplets without redundant checks, thus reducing the problem complexity compared to a naive three-loop approach, which would lead to a N^3 solution.<br>

**Comparison between 2Sum and 3Sum Problems**:<br>

In the 2 sum Problem we find the indices of two numbers of the given array which sums to the target. In the 3 sum problem we find all the unique triplets in the given array that sum to the given target. In the two sum problem, we have used two pointer approach where one pointer is at the start of the array and other at the end. In the 3 sum problem, we fix the loop and then apply two pointer approach on the remaining part of the array. But the common thing in both problems is we first sort the given array to use the pointer approach effectively.<br>

## Container With Most Water
**Problem Statement**:<br>
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).<br>
Find two lines that together with the x-axis form a container, such that the container contains the most water.<br>
Return the maximum amount of water a container can store.<br>
Notice that you may not slant the container.<br>

**Example 1**:<br>

Input: height = [1,8,6,2,5,4,8,3,7]<br>
Output: 49<br>
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water the container can contain is 49.<br>

**Solution**:<br>
~~~python
def maxArea(height):
    height = [1,8,6,2,5,4,8,3,7]
    max_area = 0

    left_index = 0
    right_index = len(height)-1

    while left_index < right_index:
        width = right_index - left_index
        low_height = min(height[left_index], height[right_index])
        area = width * low_height
        if area > max_area:
            max_area = area
        if height[left_index] <= height[right_index]:
            left_index += 1
        else:
            right_index -= 1
    return max_area

height = [1,8,6,2,5,4,8,3,7]
maxArea(height)
~~~

**Explanation**:<br>

**Initialize Pointers**: Start with left pointer at the beginning and right pointer at the end of the array.<br>
**Calculate Area**: For each pair of lines, calculate the area as the product of the distance between the pointers and the minimum height of the lines at the pointers.<br>
**Update Maximum Area**: Compare the calculated area with the maximum area and  update it only when  the calculated one is larger than the current max_area<br>
**Move Pointers**: move the pointer that points to the shorter line. This is because moving the shorter line might find a taller line, which could potentially increase the area. If the left line is shorter, Move the left pointer to the right. This might find a taller line on the left side, increasing the possible area. If the right line is shorter, Move the right pointer to the left. This might find a taller line on the right side, increasing the possible area.<br>
**result**: at the end, return the value present in the 'max_area' variable. This gives the maximum area of the given array.<br>

**Time Complexity**:<br>
The time complexity of the solution for the water container problem using the two-pointer technique is O(n). This is beacuse the technique traverse all the elements of the gicven array.<br>

**Key Insights**:<br>
The key insight of the two-pointer technique is to maximize the area by starting with the widest possible container and then narrowing the width while trying to increase the height. We always move the pointer that points to the shorter height because the area is determined by the shorter of the two heights. By moving the pointer at the shorter height, we have a chance of finding a taller height that might increase the area.<br>

**Comparing 2 sum, 3 sum and Water Container** :<br>
**2Sum and 3Sum Problems**: The movement of pointers in these problems is determined by the sum comparison with the target. Pointers move inward to increase or decrease the sum towards the target.
**Water Container Problem**: The movement of pointers is determined by the height of the lines. Pointers move to potentially find a taller line that can increase the water area.






