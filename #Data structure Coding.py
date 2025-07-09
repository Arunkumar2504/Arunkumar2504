#  Data structure Coding

from copy import copy
import math
from typing import List
from itertools import combinations
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


# Problem statement
# The N Queens puzzle is the problem of placing N chess queens on an N * N chessboard such that no two queens attack each other.

# Given an integer ‘N’, print all distinct solutions to the ‘N’ queen puzzle.

# Two queens on the same chessboard can attack each other if any of the below condition satisfies:
# 1. They share a row.
# 2. They share a column.
# 3. They share a diagonal.

def isSafe(row, col, board, n):
    for i in range(row):
        if board[i][col] == 'Q':
            return False
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1
    return True


def solveNQueensUtil(n, row, board, result):
    if row == n:
        result.append([1 if cell == 'Q' else 0 for r in board for cell in r])
        return
    for col in range(n):
        if isSafe(row, col, board, n):
            board[row] = board[row][:col] + 'Q' + board[row][col+1:]
            solveNQueensUtil(n, row + 1, board, result)
            board[row] = board[row][:col] + '.' + board[row][col+1:]


def nQueens(n):
    result = []
    board = ['.' * n for _ in range(n)]
    solveNQueensUtil(n, 0, board, result)
    return result


# ------------------------------------------------------------------------------------------------------
# Problem statement
# Given a string S containing digits from 2 to 9 inclusive. Your task is to find all possible letter combinations that the number could represent.

# A mapping from Digits to Letters(just like in Nokia 1100) is shown below. Note that 1 does not map to any letter.

def combinations(S):
    if not S:
        return []

    mapping = {
        '2': 'abc', '3': 'def', '4': 'ghi',
        '5': 'jkl', '6': 'mno',
        '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    result = []

    def backtrack(index, path):
        if index == len(S):
            result.append(path)
            return
        possible_letters = mapping[S[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)

    backtrack(0, "")
    return result

# ------------------------------------------------------------------------------------------------------
# Problem statement
# You are a coach of a group consisting of 'N' students. The ith student has a strength Arr[i]. For a Tug of War game, you want to divide students into two teams of equal size (If N is odd, then size of one team should be (N-1)/2 and size of other team should be (N+1)/2). You want a game that is fun, for this the absolute difference between the team’s strength should be as minimum as possible. A team's strength is the sum of the strengths of the students in the team.

# Detailed explanation ( Input/output format, Notes, Images )
# Constraints :
# 1 <= T <= 10
# 2 <= N <= 20
# 0 < Arr[i] <= 10^5
# Where T is the number of test cases, N is the number of students and Arr[i] is the strength of ith student.


def tugOfWar(arr, n):

    # write your code here
    total = sum(arr)
    Min_diff = float('inf')

    sizes = [n//2] if n % 2 == 0 else [n//2, n//2+1]
    for size in sizes:
        for teams in combinations(arr, size):
            team_sum = sum(teams)
            other_sum_arr = total-team_sum
            diff = abs(team_sum-other_sum_arr)
            Min_diff = min(Min_diff, diff)
    return Min_diff
# ------------------------------------------------------------------------------------------------------

# Problem statement
# Reverse a given stack of 'N' integers using recursion. You are required to make changes in the input parameter itself.


# Note: You are not allowed to use any extra space other than the internal stack space used due to recursion.


# Example:
# Input: [1,2,3,4,5]
# Output: [5,4,3,2,1]
def insertAtBottom(stack, item):
    if not stack:
        stack.append(item)
        return
    top = stack.pop()
    insertAtBottom(stack, item)
    stack.append(top)


def reverseStack(stack):
    if not stack:
        return
    top = stack.pop()
    reverseStack(stack)
    insertAtBottom(stack, top)


# ------------------------------------------------------------------------------------------------------
class point:

    def __init__(self, x, y):

        self.x = x

        self.y = y


def closestPair(cordinates, n):

    arr = [(point.x, point.y) for point in cordinates]

    # Sort based on X-coordinate

    arr.sort(key=lambda x: x[0])

    result = float('inf')

    for i in range(1, n):

        x1, y1 = arr[i - 1]

        x2, y2 = arr[i]

        result = min(result, (x2 - x1)**2 + (y2 - y1)**2)

    # Sort based on Y-coordinate

    arr.sort(key=lambda x: x[1])

    for i in range(1, n):

        x1, y1 = arr[i - 1]

        x2, y2 = arr[i]

        result = min(result, (x2 - x1)**2 + (y2 - y1)**2)

    return result
# ------------------------------------------------------------------------------------------------
# Problem statement
# You are given an input string 'S'. Your task is to find and return all possible permutations of the input string.

# Note:
# 1. The input string may contain the same characters, so there will also be the same permutations.

# 2. The order of permutation does not matter.


def findPermutations(s):
    def backtrack(path, remaining):
        if not remaining:
            permutations.append(path)
            return
        for i in range(len(remaining)):
            next_path = path + remaining[i]
            next_remaining = remaining[:i] + remaining[i+1:]
            backtrack(next_path, next_remaining)

    permutations = []
    backtrack("", s)
    return permutations
# ------------------------------------------------------------------------------------------------


# Problem statement
# Given N pairs of parentheses, write a function to generate and print all combinations of well-formed parentheses. That is , you need to generate all possible valid sets of parentheses that can be formed with a given number of pairs.
def printParenthesesHelper(cur, open_count, close_count, max_pairs):
    if len(cur) == max_pairs * 2:
        print(cur)
        return

    if open_count < max_pairs:
        printParenthesesHelper(
            cur + '{', open_count + 1, close_count, max_pairs)

    if close_count < open_count:
        printParenthesesHelper(cur + '}', open_count,
                               close_count + 1, max_pairs)


def printParantheses(n):
    printParenthesesHelper("", 0, 0, n)


# ------------------------------------------------------------------------------------------------
# Problem statement
# You are given a string 'S' containing only digits. Your task is to find all possible IP addresses that can be obtained from string 'S' in lexicographical order.

# Note:
# A valid IP address consists of exactly four integers, each integer is between 0 and 255 separated by single dots, and cannot have leading zeros except in the case of zero itself.
# For example:
# The following are valid IP addresses:
# 0.1.24.255
# 18.5.244.1

# Following are invalid IP addresses:
# 0.01.24.255  (as 01  contains one leading zero).
# 18.312.244.1 (as 312 not lies between 0 and 255).
# Detailed explanation(Input/output format, Notes, Images)
# Constraints:
# 1 <= T <= 1000
# 1 <= |S | <= 15

# Where | 'S' | denotes the length of string 'S' and 'S' contains only digits from 0 to 9.

# Time Limit: 1 sec
# Note:
# You do not need to print anything, it has already been taken care of. Just implement the given function.
# Sample Input 1:
# 2
# 2122
# 23579
# Sample Output 1:
# [“2.1.2.2”]
# [“2.3.5.79”, “2.3.57.9”, “2.35.7.9”, “23.5.7.9”]
# Explanation for sample Input 1:
# For the first test case, there is only one possible IP address that is [2.1.2.2]

# For the second test case, all possible IP addresses are shown below.
# [2.3.5.79], [2.3.57.9], [2.35.7.9], [23.5.7.9]
# Sample Input 2:
# 2
# 123
# 02300
# Sample Output 2:
# []
# [“0.2.30.0”, “0.23.0.0”]
# Explanation for sample Input 2:
# For the first test case, there is no possible IP address. Therefore then answer is []

# For the second test case, there are only 2 possible IP addresses are shown below.
# [0.2.30.0], [0.23.0.0]

def isValid(segment):
    # Check if the segment is a valid IP section
    if len(segment) > 1 and segment[0] == '0':
        return False  # leading zero
    if int(segment) > 255:
        return False
    return True


def generateIPAddress(s):
    n = len(s)
    result = []

    # Try all combinations for 3 dots to split into 4 parts
    for i in range(1, min(4, n - 2)):
        for j in range(i + 1, min(i + 4, n - 1)):
            for k in range(j + 1, min(j + 4, n)):
                a = s[:i]
                b = s[i:j]
                c = s[j:k]
                d = s[k:]
                if all(map(isValid, [a, b, c, d])):
                    result.append(a + "." + b + "." + c + "." + d)

    return sorted(result)
# -------------------------------------------------------------------------------------------------


# Problem statement
# You are given a string 'STR' containing lowercase English letters from a to z inclusive. Your task is to find all non-empty possible subsequences of 'STR'.

# A Subsequence of a string is the one which is generated by deleting 0 or more letters from the string and keeping the rest of the letters in the same order.
def subsequences(string):
    result = []
    n = len(string)

    def backtrack(index, path):
        if index == n:
            if path:
                result.append(path)
            return
        # Include current character
        backtrack(index + 1, path + string[index])
        backtrack(index + 1, path)

    backtrack(0, "")
    return result

# -------------------------------------------------------------------------------------------------


# Problem statement
# You are given an array 'ARR' of 'N' distinct positive integers. You are also given a non-negative integer 'B'.


# Your task is to return all unique combinations in the array whose sum equals 'B'. A number can be chosen any number of times from the array 'ARR'.


# Elements in each combination must be in non-decreasing order.


def combSum(ARR, B):
    ARR.sort()
    result = []

    def backtrack(start, target, path):
        if target == 0:
            result.append(copy(path))
            return
        for i in range(start, len(ARR)):
            if ARR[i] > target:
                break
            path.append(ARR[i])
            # Not i+1 because we can reuse same element
            backtrack(i, target - ARR[i], path)
            path.pop()  # Backtrack

    backtrack(0, B, [])
    return result
# --------------------------------------------------------------------------------------------------


# Problem statement
# Ninja has been given a binary string ‘STR’ containing either ‘0’ or ‘1’. A binary string is called beautiful if it contains alternating 0s and 1s.

# For Example: ‘0101’, ‘1010’, ‘101’, ‘010’ are beautiful strings.


# Your task is to determine the minimum number of operations Ninja should perform to make ‘STR’ beautiful.


# Minimum operations to make ‘STR’ ‘0010’ beautiful is ‘1’. In one operation, we can convert ‘0’ at index ‘0’ (0-based indexing) to ‘1’. The ‘STR’ now becomes ‘1010’ which is a beautiful string.

def makeBeautiful(str):

    n = len(str)
    count1 = 0
    count2 = 0

    for i in range(n):
        expected1 = '0' if i % 2 == 0 else '1'
        expected2 = '1' if i % 2 == 0 else '0'
        if str[i] != expected1:
            count1 += 1
        if str[i] != expected2:
            count2 += 1

    return min(count1, count2)

# --------------------------------------------------------------------------------------------------


# Problem statement alice and bob sum
# Alice and Bob recently studied bitwise operators and were extremely fascinated by them. Alice found the following function in a book:

# function magic(P, Q):

# while Q > 0:

# A = P AND Q

# B = P XOR Q

# Q = A * 2

# P = B

# return P

# Alice wondered how many times the while loop would run for any value of ‘P’ and ‘Q’. Alice gave Bob the binary representation of ‘P’ and ‘Q’ and asked him to help her count this.

# Help Bob count the number of times the while loop would run for the given value of ‘P’ and ‘Q’.
def countLoop(p: str, q: str) -> int:
    # Write your code here.
    P = int(p, 2)
    Q = int(q, 2)
    count = 0

    while Q > 0:
        A = P & Q
        B = P ^ Q
        Q = A << 1
        P = B
        count += 1
    return count
# ---------------------------------------------------------------------------------------------------

# Problem statement
# You are given an array containing 'N' points in the plane. The task is to find out the distance of the closest points.

# Where distance between two points (x1, y1) and (x2, y2) is calculated as [(x1 - x2) ^ 2] + [(y1 - y2) ^ 2].


def closest_pair_sum(points):
    def dist(p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

    def brute_force(pts):
        min_d = float('inf')
        for i in range(len(pts)):
            for j in range(i + 1, len(pts)):
                min_d = min(min_d, dist(pts[i], pts[j]))
        return min_d

    def strip_closest(strip, d):
        min_d = d
        strip.sort(key=lambda x: x[1])  # sort by y
        for i in range(len(strip)):
            j = i + 1
            while j < len(strip) and (strip[j][1] - strip[i][1]) ** 2 < min_d:
                min_d = min(min_d, dist(strip[i], strip[j]))
                j += 1
        return min_d

    def closest_utill(pts_sorted_x):
        n = len(pts_sorted_x)
        if n <= 3:
            return brute_force(pts_sorted_x)

        mid = n // 2
        mid_x = pts_sorted_x[mid][0]

        dl = closest_utill(pts_sorted_x[:mid])
        dr = closest_utill(pts_sorted_x[mid:])
        d = min(dl, dr)

        strip = [p for p in pts_sorted_x if (p[0] - mid_x) ** 2 < d]

        return min(d, strip_closest(strip, d))

    points.sort()
    return closest_utill(points)


if __name__ == "__main__":
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    print(closest_pair_sum(points))

# ---------------------------------------------------------------------------------------------------------------

# Problem statement
# You are given an array “ARR” of size N. Your task is to find out the sum of maximum and minimum elements in the array.

# Can you do the above task in a minimum number of comparisons?
# Detailed explanation
# Constraints:
# 1 <= T <= 10
# 1 <= N <= 10^5
# -10^9 <= ARR[i] <= 10^9


def sumOfMaxMin(arr):
    n = len(arr)
    if n % 2 == 0:
        if arr[0] < arr[1]:
            mn = arr[0]
            mx = arr[1]
        else:
            mn = arr[1]
            mx = arr[0]
        i = 2
    else:
        mn = mx = arr[0]
        i = 1
    while i < n-1:
        if arr[i] < arr[i+1]:
            small = arr[i]
            large = arr[i+1]
        else:
            small = arr[i+1]
            large = arr[i]
        if small < mn:
            mn = small
        if large > mx:
            mx = large
        i += 2
    return mn+mx


# ---------------------------------------------------------------------------------------------------------------
# Reverse_by_position
arr = [1, 2, 3, 6, 5, 4, 7, 8]
m = 3


def Reverse_by_position(arr, m):
    array_of_value = arr[:m+1]
    for i in range(len(arr)):
        if arr[i] == arr[m]:
            rev = arr[:m:-1]
            array_of_value.extend(rev)
            break
    return array_of_value


print(Reverse_by_position(arr, m))

# -----------------------------------------------------------------------------------------------------------------
