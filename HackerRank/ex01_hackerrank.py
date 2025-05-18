"""
HackerRank - Python If-Else

Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
"""

number = int(input(""))

if number % 2 == 1:
    print("Weird")
else:
    if number in range(2, 6):
        print("Not Weird")
    elif number in range(6, 21):
        print("Weird")
    else:
        print("Not Weird")
