def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]
    return [] 

# O(n^2)

print(two_sum([2, 11, 7, 15], 9))


def isValid(s):
    if len(s) % 2 != 0: # the length is odd ex: ()[
        return False
    # create a stack and a head = 0
    stack = []
    for c in s:
        if c == '(':
            stack.append(')')
        elif c == '[':
            stack.append(']')
        elif c == '{':
            stack.append('}')
        else:
            if not stack: # if we dont see a closing bracket but the stack is empty
                return False
            if stack.pop() != c: #pop that last expected closing bracket and check it
                return False
    return len(stack) == 0

print(isValid("()[]{}"))


# import Counter
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    map = {}
    for char in s:
        map[char] = map.get(char, 0) + 1
    for char in t:
        if char not in map:
            return False
        map[char]-=1
        if map[char] < 0: # if the count drops below 0 then t has more copies of this char than s
            return False
    return True
    # if Counter(s) == Counter(t): 
    #     return True 
    # return False

print(isAnagram("anagram", "nagaram"))



def isPalindrome(x):

    if (x < 0 or x != 0 and x % 10 == 0):
        return False
    s = str(x)
    l = 0
    r = len(s) - 1

    while l < r:
        if s[l] != s[r]:
            return False
        l+=1
        r-=1
    return True

print(isPalindrome(121))

# ------------------ LINKEDLIST -------------
class ListNode:
    def __init__(self, val, next=None):
        self.val = val 
        self.next = next
def mergeTwoLists(list1, list2):

    dummy = ListNode(0)
    current = dummy

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next 

        current = current.next 
    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    return dummy.next

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head
def print_linked_list(head):
    elements = []
    while head:
        elements.append(str(head.val))
        head = head.next
    print(" -> ".join(elements))

# 🚀 1. Convert your Python lists into ListNode objects
l1 = create_linked_list([1, 2, 4])
l2 = create_linked_list([1, 3, 4])

# 🚀 2. Run your merge function
merged_head = mergeTwoLists(l1, l2)

# 🚀 3. Print the result
print_linked_list(merged_head)

# ------------------------------------------------------------------------------




def removeDuplicates(nums):
    if not nums:
        return 0

    k = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[k]:
            k+=1
            nums[k] = nums[i]
    return k + 1

print(removeDuplicates([1, 1, 2, 3, 4, 5, 5, 6]))
