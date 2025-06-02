#  Data structure Coding

from math import *
from collections import *
from sys import *
from os import *
import array

Array = array.array('i', [10, 20, 30, 40, 50])
# Accessing elements
print(Array[0])

# --------------------------------------------------------------------------------------------


# Displaying all elements
for i in range(len(Array)):
    print(Array[i])
# --------------------------------------------------------------------------------


# # Adding elements and displaying
Array.append(60)
for i in range(len(Array)):
    print(Array[i])
# --------------------------------------------------------------------------------


# # Searching for a number and index in the array
i = 0
Finding_number = int(input("Please enter the number you want to find: "))
for i in range(len(Array)):
    if Array[i] == Finding_number:
        print(f"Yes, the number is present in {i} index in the array.")
        i += 1
        break
    elif Array[i] != Finding_number:
        print(f"Your Number is not in {i} index")
# --------------------------------------------------------------------------------


# Problem statement
# You are given an array ‘arr’ containing ‘n’ integers. You are also given an integer ‘num’, and your task is to find whether ‘num’ is present in the array or not .


# If ‘num’ is present in the array, return the 0-based index of the first occurrence of ‘num’. Else, return -1.


# Example:
# Input: ‘n’ = 5, ‘num’ = 4
# 'arr' = [6, 7, 8, 4, 1]

# Output: 3

# Explanation:
# 4 is present at the 3rd index.
# Detailed explanation(Input/output format, Notes, Images)
# Sample Input 1:
# 5 4
# 6 7 8 4 1
# Sample Output 1:
# 3
# Explanation Of Sample Input 1:
# 4 is present at the 3rd index.
def linearSearch(n: int, num: int, arr: [int]) -> int:  # type: ignore
    # Write your code here.
    Index_value = arr.index(num)
    print(Index_value)
    pass


n = int(input("Please enter the number of elements in the array: "))
num = int(input("Please enter the number you want to find: "))
arr = list(map(int, input("Please enter the lists: ").split()))

linearSearch(n=n, num=num, arr=arr)
# --------------------------------------------------------------------------------


# Problem statement
# Given an array of size N, find the sum of its elements.


n = int(input())
N = list(map(int, input().split()))
total = sum(N)
print(total)


# Function to find the largest element
def largestElement(arr, n):
    max_element = arr[0]  # Assume the first element is the largest

    for i in range(1, n):
        if arr[i] > max_element:
            max_element = arr[i]

    return max_element


# ---- Main code ----
# Take input
n = int(input())                       # First line: number of elements
arr = list(map(int, input().split()))  # Second line: space-separated elements

# Call the function and print the result
print(largestElement(arr, n))

# ---------------------------------------------------------------------------


# Problem statement
# You are given a string 'STR'. You have to convert the first alphabet of each word in a string to UPPER CASE.

# For example:

# If the given string 'STR' = ”I am a student of the third year” so you have to transform this string to ”I Am A Student Of The Third Year"
# Note:

# 'STR' will contains only space and alphabets both uppercase and lowercase. The words will be separated by space.


def convertString(s):
    words = s.split()
    result_words = []
    for w in words:
        if len(w) > 0:
            new_word = w[0].upper() + w[1:]
            result_words.append(new_word)
        else:
            result_words.append(w)
    return " ".join(result_words)

# T = int(input().strip())
# for _ in range(T):
#     s = input().strip()
#     print(convertString(s))

# --------------------------------------------------------------------------------------------


# Problem statement
# You are given two non-negative integers, ‘NUM1’ and ‘NUM2’, in the form of strings. Return the sum of both strings.


# Note:
# You do not need to print anything, it has already been taken care of. Just implement the given function.
# Example:
# Let ‘NUM1’ be: “5”
# Let ‘NUM2’ be: “21”
# The sum of both numbers will be: “26”.

def stringSum(num1: str, num2: str) -> str:
    # Write your code here.
    Int_Change_one = int(num1)
    Int_Change_two = int(num2)
    sum_result = Int_Change_one + Int_Change_two
    return str(sum_result)  # Convert the sum back to string and return it


print(stringSum("123", "456"))

# ---------------------------------------------------------------------------------------------

# Problem statement
# You are given a singly linked list and an integer ‘K’. Your task is to search for the integer ‘K’ in the linked list. If it is present, return 1; otherwise, return 0.
# Note:
# The linked list is 0-indexed, meaning the first node is at index 0.
# You do not need to print anything, it has already been taken care of. Just implement the given function.
# Definition for singly-linked list.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def searchInLinkedList(head, k):
    current = head
    while current is not None:
        if current.data == k:
            return 1
        current = current.next
    return 0

# ---------------------------------------------------------------------------------------------


# Problem statement
# Given a singly linked list of 'N' nodes. The objective is to determine the middle node of a singly linked list. However, if the list has an even number of nodes, we return the second middle node.

# Note:
# 1. If the list is empty, the function immediately returns None because there is no middle node to find.
# 2. If the list has only one node, then the only node in the list is trivially the middle node, and the function returns that node.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def findMiddle(head):
    if head is None:
        return None
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# ---------------------------------------------------------------------------------------------

# Problem statement
# You are given a Singly Linked List of integers. You need to reverse the Linked List by changing the links between nodes.

# Note:
# You do not need to print anything, just return the head of the reversed linked list.


def reverseLinkedList(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

# ---------------------------------------------------------------------------------------------


# Problem statement
# Ninja is learning the binary representation of the numbers. He wanted to practice the topic, so he picked a question. The problem statement says, two numbers, ‘A’ and ‘B’ are given. Find the number of bits of ‘B’ that should be flipped to convert it into ‘A’.Can you help Ninja to solve this problem?

# You are given two integers, ‘A’ and ‘B’.Find the number of bits of ‘B’ that should be flipped to convert it into ‘A’.

# For Example
# If ‘A’ is 13(1101) and ‘B’ is 7(0111), The number of bits that should be flipped is 2(0111).

def numberOfFlips(a: int, b: int) -> int:

    # Write your code here.
    xor_value = a ^ b

    return bin(xor_value).count("1")

# ---------------------------------------------------------------------------------------------


# Problem statement
# Given valid mathematical expressions in the form of a string. You are supposed to return true if the given expression contains a pair of redundant brackets, else return false. The given string only contains ‘(‘, ’)’, ‘+’, ‘-’, ‘*’, ‘/’ and lowercase English letters.

# Note:
# A pair of brackets is said to be redundant when a subexpression is surrounded by needless / useless brackets.

# For Example:
# ((a+b)) has a pair of redundant brackets. The pair of brackets on the first and last index is needless.
# While(a + (b*c)) does not have any pair of redundant brackets.


def findRedundantBrackets(s: str):
    # Write your code here
    stack = []
    for i in s:
        if i == ')':
            top = stack.pop()
            Operation_found = False
            while top != "(":
                if top in "+-*/":
                    Operation_found = True
                top = stack.pop()
            if not Operation_found:
                return True
        else:
            stack.append(i)
    return False

# ----------------------------------------------------------------------------------------------


# Problem statement
# Design a data structure to implement deque of size ‘N’. It should support the following operations:

# pushFront(X): Inserts an element X in the front of the deque. Returns true if the element is inserted, otherwise false.

# pushRear(X): Inserts an element X in the back of the deque. Returns true if the element is inserted, otherwise false.

# popFront(): Pops an element from the front of the deque. Returns - 1 if the deque is empty, otherwise returns the popped element.

# popRear(): Pops an element from the back of the deque. Returns - 1 if the deque is empty, otherwise returns the popped element.

# getFront(): Returns the first element of the deque. If the deque is empty, it returns - 1.

# getRear(): Returns the last element of the deque. If the deque is empty, it returns - 1.

# isEmpty(): Returns true if the deque is empty, otherwise false.

# isFull(): Returns true if the deque is full, otherwise false.
# Following types of queries denote these operations:

# Type 1: for pushFront(X) operation.
# Type 2: for pushRear(X) operation.
# Type 3: for popFront() operation.
# Type 4: for popRear() operation.
# Type 5: for getFront() operation.
# Type 6: for getRear() operation.
# Type 7: for isEmpty() operation.
# Type 8: for isFull() operation.
# Detailed explanation(Input/output format, Notes, Images)
# Constraints:
# 1 <= N <= 1000
# 1 <= Q <= 10 ^ 5
# 1 <= P <= 8
# 1 <= X <= 10 ^ 5

# Time Limit: 1 sec

# Where ‘N’ represents the size of the deque, ‘Q’ represents the number of queries, ‘P’ represents the type of operation and ‘X’ represents the element.


class Deque:
    def __init__(self, size):
        self.size = size
        self.arr = [0] * size
        self.front = -1
        self.rear = -1

    def isFull(self):
        return ((self.front == 0 and self.rear == self.size - 1) or
                (self.rear + 1) % self.size == self.front)

    def isEmpty(self):
        return self.front == -1

    def pushFront(self, x):
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = self.rear = 0
        elif self.front == 0:
            self.front = self.size - 1
        else:
            self.front -= 1
        self.arr[self.front] = x
        return True

    def pushRear(self, x):
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = self.rear = 0
        elif self.rear == self.size - 1:
            self.rear = 0
        else:
            self.rear += 1
        self.arr[self.rear] = x
        return True

    def popFront(self):
        if self.isEmpty():
            return -1
        popped = self.arr[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        elif self.front == self.size - 1:
            self.front = 0
        else:
            self.front += 1
        return popped

    def popRear(self):
        if self.isEmpty():
            return -1
        popped = self.arr[self.rear]
        if self.front == self.rear:
            self.front = self.rear = -1
        elif self.rear == 0:
            self.rear = self.size - 1
        else:
            self.rear -= 1
        return popped

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.arr[self.front]

    def getRear(self):
        if self.isEmpty():
            return -1
        return self.arr[self.rear]
