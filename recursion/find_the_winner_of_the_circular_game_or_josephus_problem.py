"""
Recursion - Find the Winner of the Circular Game

Description: There are n friends that are playing a game. The friends are sitting in a circle and are 
numbered from 1 to n in clockwise order. More formally, moving clockwise from the ith friend brings you 
to the (i+1)th friend for 1 <= i < n, and moving clockwise from the nth friend brings you to the 1st 
friend.

The rules of the game are as follows:
1. Start at the 1st friend.
2. Count the next k friends in the clockwise direction including the friend you started at. The counting 
wraps around the circle and may count some friends more than once.
3. The last friend you counted leaves the circle and loses the game.
4. If there is still more than one friend in the circle, go back to step 2 starting from the friend 
immediately clockwise of the friend who just lost and repeat.
5. Else, the last friend in the circle wins the game.

Given the number of friends, n, and an integer k, return the winner of the game.

Example: 
Input: n = 5, k = 2
Output: 3
Explanation: Here are the steps of the game:
1) Start at friend 1.
2) Count 2 friends clockwise, which are friends 1 and 2.
3) Friend 2 leaves the circle. Next start is friend 3.
4) Count 2 friends clockwise, which are friends 3 and 4.
5) Friend 4 leaves the circle. Next start is friend 5.
6) Count 2 friends clockwise, which are friends 5 and 1.
7) Friend 1 leaves the circle. Next start is friend 3.
8) Count 2 friends clockwise, which are friends 3 and 5.
9) Friend 5 leaves the circle. Only friend 3 is left, so they are the winner.

Time Complexity - O(N)
Space Complexity - O(N)

LeetCode link: https://leetcode-cn.com/problems/find-the-winner-of-the-circular-game
"""
from collections import deque 

def find_the_winner_deque(n: int, k: int) -> int:
    q = deque(range(1, n + 1))
    while len(q) > 1:
        for _ in range(k - 1):
            q.append(q.popleft())
        q.popleft()
    
    return q[0]

def find_the_winner_recursion(n: int, k: int) -> int:
    def find_winner_with_start_point(arr, start_point, k):
        if len(arr) == 1:
            return arr[0]
        
        leaver_index = (start_point + k - 1) % len(arr)
        arr.pop(leaver_index)
        start_point = leaver_index

        return find_winner_with_start_point(arr, start_point, k)
    

    return find_winner_with_start_point([i for i in range(1, n+1)], 0, k)

def find_the_winner_math_recursion(n: int, k: int) -> int:
    pass

def find_the_winner_math_iteration(n: int, k: int) -> int:
    pass


if __name__ == "__main__":
    print(f"winner of n = 5, k = 2 is: {find_the_winner_deque(5, 2)}")
    print(f"winner of n = 5, k = 2 is: {find_the_winner_recursion(5, 2)}")
    print(f"winner of n = 5, k = 2 is: {find_the_winner_math_recursion(5, 2)}")
    print(f"winner of n = 5, k = 2 is: {find_the_winner_math_iteration(5, 2)}")
