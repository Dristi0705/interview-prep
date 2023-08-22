"""This program shows different ways to find a duplicate number in an array.

Consideration -> array is of length n + 1 with elements [1, n].
One number is duplicate, and we need to return it.

"""

from typing import List


def duplicates_using_sort(nums: List[int]) -> int:
    """Sort the array. And iterate over from 1st element and check with curr - 1
    element. If same, we know it is the duplicate.
    Time complexity would O(nlogn) - merge sort"""

    nums.sort()

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return nums[i]


def duplicates_using_set(nums: List[int]) -> int:
    """Using a set, we can lookup at numbers we have seen already.
    This is efficient from time as it runs in O(n) time but requires a O(n)
    extra space"""

    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)


def duplicates_using_negative_marking(nums: List[int]) -> int:
    """Mark indexes negative, if we have seen the value. So we take first abs value of element 1
    and mark nums[1] = -nums[1].

    We take abs value to make sure we are taking the right element. While updating, if we find the num in the
    location already negative, we know that we have seen this value before.

    But this will always work with arrays with all positive integers.
    """

    for i in range(len(nums)):
        num = abs(nums[i])
        if nums[num] < 0:
            return num
        nums[num] = -nums[num]

def duplicates_using_hare_tortoise(nums: List[int]) -> int:
    """
    This method will work when the array is immutable and we still need to achieve O(n) Time and O(1) Space complexity
    
    We detect the start point of loop in the list with a linking rule nums[i] -> nums[nums[i]]
    The Hare moves with twice the speed of tortoise . So hare = nums[nums[hare]] while tortoise = nums[tortoise]
    at each updation step. If they collide there is a loop in the linked list with the above rule,
    and hence, a duplicate in the array. The start point of the loop will be our duplicate element.
    """

    # Initialise variables
    tortoise = nums[0]
    hare = nums[0]
 
    # Loop till we find the
    # duplicate element
    while (1):
 
        tortoise = nums[tortoise]
 
        # Hare moves with twice
        # the speed of tortoise
        hare = nums[nums[hare]]
        if (tortoise == hare):
            break
 
    tortoise = nums[0]
 
    # Loop to get start point
    # of the cycle as start
    # point will be the duplicate
    # element
    while (tortoise != hare):
        tortoise = nums[tortoise]
        hare = nums[hare]
        
    return tortoise


# Tests
nums = [1, 2, 3, 4, 4, 5]
print("duplicates_using_sort", duplicates_using_sort(nums))
print("duplicates_using_set", duplicates_using_set(nums))
print("duplicates_using_negative_marking", duplicates_using_negative_marking(nums))
print("duplicates_using_hare_tortoise", duplicates_using_hare_tortoise(nums))
