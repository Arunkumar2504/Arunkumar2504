#  Data structure Coding

from sys import stdin
import sys
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

# ---------------------------------------------------------------------------------------

# Factorial


def Factorial(n):
    if n == 0 or n == 1:
        return 1
    return n*Factorial(n-1)


print(Factorial(5))  # Output: 120

# ---------------------------------------------------------------------------------------
# Problem statement
# You are given three rods(numbered 1 to 3), and ‘N’ disks initially placed on the first rod, one on top of each other in increasing order of size(the largest disk is at the bottom). You are supposed to move the ‘N’ disks to another rod(either rod 2 or rod 3) using the following rules and in less than 2 ^ (N) moves.

# 1. You can only move one disk in one move.
# 2. You can not place a larger disk on top of a smaller disk.
# 3. You can only move the disk at the top of any rod.
# Note:
# You may assume that initially, the size of the ‘i’th disk from the top of the stack is equal to ‘i’, i.e. the disk at the bottom has size ‘N’, the disk above that has size ‘N - 1’, and so on. The disk at the top has size 1.


def towerOfHanoi(n):
    moves = []

    def solve(n, source, target, helper):
        if n == 1:
            moves.append([source, target])
            return
        solve(n - 1, source, helper, target)
        moves.append([source, target])
        solve(n - 1, helper, target, source)

    solve(n, 1, 2, 3)
    return moves
# ---------------------------------------------------------------------------------------------------------------------------------------------------


# Problem statement
# Given an integer array 'ARR' of size 'N' and an integer 'K', return all the subsets of 'ARR' which sum to 'K'.

# Subset of an array 'ARR' is a tuple that can be obtained from 'ARR' by removing some(possibly all) elements of 'ARR'.

# Note:
# The order of subsets is not important.

# The order of elements in a particular subset should be in increasing order of the index.


def findSubsetsThatSumToK(arr, n, k):
    result = []

    def backtrack(index, current_subset, current_sum):
        if index == n:
            if current_sum == k:
                result.append(current_subset[:])
            return

        current_subset.append(arr[index])
        backtrack(index + 1, current_subset, current_sum + arr[index])

        current_subset.pop()
        backtrack(index + 1, current_subset, current_sum)

    backtrack(0, [], 0)
    return result
# ---------------------------------------------------------------------------------------------------------------------------------------------------


# Problem statement
# You have given two positive integers N and K. Your task is to print a series of numbers i.e subtract K from N until it becomes 0 or negative then add K until it becomes N. You need to do this task without using any loop.

# For Example:
# For  N = 5, K = 2
# Series = [5, 3, 1, -1, 1, 3, 5]

def printSeries(n, k, original=None, decreasing=True):
    if original is None:
        original = n

    # Base case: when we reach 0 or negative while decreasing
    if decreasing and n <= 0:
        # start increasing now
        return [n] + printSeries(n + k, k, original, False)

    # Base case: when we reach back to original while increasing
    if not decreasing and n == original:
        return [n]

    if decreasing:
        return [n] + printSeries(n - k, k, original, True)
    else:
        return [n] + printSeries(n + k, k, original, False)

# ------------------------------------------------------------------------------------------------------------


# Problem statement
# You are given the first term(A), the common ratio(R) and an integer N. Your task is to find the Nth term of the GP series.

# The general form of a GP(Geometric Progression) series is A, A(R), A(R ^ 2), A*(R ^ 3) and so on where A is the first term of GP series

# Note:
# As the answer can be large enough, return the answer modulo 10 ^ 9 + 7.


MOD = 10**9 + 7

# Fast modular exponentiation: r^(n-1) % MOD


def power(r, exp):
    result = 1
    r = r % MOD
    while exp > 0:
        if exp % 2 == 1:
            result = (result * r) % MOD
        r = (r * r) % MOD
        exp //= 2
    return result


def nthTermOfGP(n, a, r):
    if a == 0:
        return 0
    if r == 0:
        return 0 if n > 1 else a
    return (a * power(r, n - 1)) % MOD


t = int(sys.stdin.readline().strip())

while (t > 0):

    n, a, r = map(int, input().split())
    print(nthTermOfGP(n, a, r))

    t = t - 1
# ------------------------------------------------------------------------------------------------------------

# Problem statement
# Aakash is a member of Ninja club. He has a weird family structure. Every male member(M) gives birth to a male child first and then a female child, whereas every female(F) member gives birth to a female child first and then to a male child. Aakash analyses this pattern and wants to know what will be the Kth child in his Nth generation. Can you help him?

# A sample generation tree is shown, where ‘M’ denotes the male member and ‘F’ denotes the female member.


def kthChildNthGeneration(n, k):
    if n == 1:
        return "Male"

    parent = kthChildNthGeneration(n - 1, (k + 1) // 2)

    if parent == "Male":
        return "Male" if k % 2 == 1 else "Female"
    else:
        return "Female" if k % 2 == 1 else "Male"


# ------------------------------------------------------------------------------------------------------------
# Problem statement
# You have been given a 9 X 9 2D matrix 'MATRIX' with some cells filled with digits(1 - 9), and some empty cells(denoted by 0).

# You need to find whether there exists a way to fill all the empty cells with some digit(1 - 9) such that the final matrix is a valid Sudoku solution.

# A Sudoku solution must satisfy all the following conditions-

# 1. Each of the digits 1 - 9 must occur exactly once in each row.
# 2. Each of the digits 1 - 9 must occur exactly once in each column.
# 3. Each of the digits 1 - 9 must occur exactly once in each of the 9, 3 x 3 sub-matrices of the matrix.
# Note
# 1. There will always be a cell in the matrix which is empty.
# 2. The given initial matrix will always be consistent according to the rules mentioned in the problem statement.
# Detailed explanation(Input/output format, Notes, Images)
# Constraints:
# 1 <= 'T' <= 5
# N = 9
# 0 <= MATRIX[i][j] <= 9

# Where 'N' denotes the size of the given square matrix.

# Time Limit: 1sec
# Sample Input 1:
# 1
# 9 0 0 0 2 0 7 5 0
# 6 0 0 0 5 0 0 4 0
# 0 2 0 4 0 0 0 1 0
# 2 0 8 0 0 0 0 0 0
# 0 7 0 5 0 9 0 6 0
# 0 0 0 0 0 0 4 0 1
# 0 1 0 0 0 5 0 8 0
# 0 9 0 0 7 0 0 0 4
# 0 8 2 0 4 0 0 0 6
# Sample Output 1:
# yes
# Explanation of the Sample Input1:
# One of the possible solutions is :
# 9 4 1 3 2 6 7 5 8
# 6 3 7 1 5 8 2 4 9
# 8 2 5 4 9 7 6 1 3
# 2 6 8 7 1 4 3 9 5
# 1 7 4 5 3 9 8 6 2
# 3 5 9 6 8 2 4 7 1
# 4 1 3 2 6 5 9 8 7
# 5 9 6 8 7 3 1 2 4
# 7 8 2 9 4 1 5 3 6
# Sample Input 2:
# 1
# 1 5 9 0 0 6 0 3 2
# 2 7 4 0 0 0 0 0 0
# 3 8 6 2 0 0 0 0 5
# 4 9 2 5 0 1 0 8 0
# 6 3 7 0 4 0 0 0 0
# 5 1 0 8 2 0 0 0 0
# 8 2 1 0 0 0 0 0 0
# 7 6 0 1 0 0 4 2 0
# 9 4 3 0 7 0 0 6 1
# Sample Output 2:
# no
# Explanation of the Sample Input2:
# In the third column from the left, there are two empty cells out of which one has to be filled with ‘8’, but we can’t put 8 in any of those two cells.

def isItSudoku(board):
    def is_valid(matrix, row, col, num):
        for x in range(9):
            if matrix[row][x] == num or matrix[x][col] == num:
                return False

        startRow = row - row % 3
        startCol = col - col % 3
        for i in range(3):
            for j in range(3):
                if matrix[startRow + i][startCol + j] == num:
                    return False

        return True

    def solve(matrix):
        for i in range(9):
            for j in range(9):
                if matrix[i][j] == 0:
                    for num in range(1, 10):
                        if is_valid(matrix, i, j, num):
                            matrix[i][j] = num
                            if solve(matrix):
                                return True
                            matrix[i][j] = 0
                    return False
        return True

    return solve(board)
# ------------------------------------------------------------------------------------------------------------


# Problem statement
# Given a source point(sx, sy) and a destination point(dx, dy), the task is to check if it is possible to reach the destination point using the following valid moves:

# (a, b) -> (a + b, b)
# (a, b) -> (a, a + b)
# Your task is to find if it is possible to reach the destination point using only the desired moves or not .

# For example:
# For the coordinates, source point = (1, 1) and destination point = (3, 5)
# The output will be true as the destination point can be reached using the following sequence of moves:
# (1, 1) -> (1, 2) -> (3, 2) -> (3, 5)

def reachDestination(sx, sy, dx, dy):
    while dx >= sx and dy >= sy:
        if dx == sx and dy == sy:
            return True
        if dx > dy:
            if dy == sy:
                return (dx - sx) % dy == 0
            dx %= dy
        else:
            if dx == sx:
                return (dy - sy) % dx == 0
            dy %= dx
    return False


# -------------------------------------------------------------------------------------------------------------------
# Problem statement
# You are given a 2-D matrix consisting of 0’s and 1’s with ‘N’ rows and ‘N’ columns, you are supposed to find all paths from the cell(0, 0)(top-left cell) to the cell(N-1, N-1)(bottom-right cell). All cells with value 0 are blocked and cannot be travelled through while all cells with value 1 are open.

# If you are currently at cell (x, y) then you can move to (x+1,y)(denoted by ‘D’), (x-1,y)(denoted by ‘U’), (x,y+1)(denoted by ‘R’), (x,y-1)(denoted by ‘L’) in one move. You cannot move out of the grid.

def isValid(arr, i, j, n, visited):
    return 0 <= i < n and 0 <= j < n and arr[i][j] == 1 and visited[i][j] == 0


def solve(arr, i, j, n, path, paths, visited, co_or):
    if i == n - 1 and j == n - 1:
        paths.append(path)
        return

    for dx, dy, move in co_or:
        ni, nj = i + dx, j + dy
        if isValid(arr, ni, nj, n, visited):
            visited[ni][nj] = 1
            solve(arr, ni, nj, n, path + move, paths, visited, co_or)
            visited[ni][nj] = 0


def findAllPaths(arr):
    paths = []
    n = len(arr)
    visited = [[0 for _ in range(n)] for _ in range(n)]
    co_or = [(1, 0, "D"), (0, -1, "L"), (0, 1, "R"), (-1, 0, "U")]

    if arr[0][0] == 1:
        visited[0][0] = 1
        solve(arr, 0, 0, n, "", paths, visited, co_or)

    return sorted(paths)
# ------------------------------------------------------------------------------------------------------