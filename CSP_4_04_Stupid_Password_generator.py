"""
Problem: Stupid Password Generator
Write a program that enters two integers n and l and generates, in alphabetical order, all possible "stupid” passwords" that consist of the following 5 characters:

Character 1: a digit from 1 to n.
Character 2: a digit from 1 to n.
Character 3: a small letter from the first l letters of the Latin alphabet.
Character 4: a small letter from the first l letters of the Latin alphabet.
Character 5: a digit from 1 to n, greater than the first 2 digits.
Input Data
The input is read as arguments and consists of two integers: n and l within the range [1 … 9].Screenshot 2025-10-07 at 10.53.33 AM.png

Output Data
Return a list of all "stupid" passwords in alphabetical order.
"""

def stupidPassword(n: int, l: int):
    allpassword = []
    password = ""
    alphabet = ["a","b","c","d","e","f","g","h","i"]
    firstnum = 1
    secondnum = 1
    firstletter = 0
    secondletter = 0

    while firstnum < n + 1:
        for lastnum in range(max(firstnum, secondnum) + 1, n + 1):
            password = password + str(firstnum)
            password = password + str(secondnum)
            password = password + alphabet[firstletter]
            password = password + alphabet[secondletter]
            password = password + str(lastnum)

            allpassword.append(password)
            password = ""

        secondletter += 1
        if secondletter == l:
            secondletter = 0
            firstletter += 1

        if firstletter == l:
            firstletter = 0
            secondnum += 1

        if secondnum == n + 1:
            secondnum = 1
            firstnum += 1

    allpassword.sort()
    print(allpassword)
    return allpassword
stupidPassword(2,4)
