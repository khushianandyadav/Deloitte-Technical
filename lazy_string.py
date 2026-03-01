'''
Problem Statement :

Anish is the laziest person you can ever see. He is tasked to write the name of the winner in a game where two people take part. And he just writes the longest common subsequence over there, so that with minimum chane or no backspace he can edit the name to the winner’s name.
For two given names, you have to predict what Anish will write in his computer before the start of the name. If there are more than two longest subsequences possible,write the one with less lexicographic value.
Input Format:
Two lines including two strings of name(All with capital letters)

Output Format:
A single line with the lexicographically smallest possible longest common subsequence.

Sample Input:
ABCD
BACD
Sample Output:
ACD
Exclamation:
ACD and BCD these are the two possible biggest substring
'''

s1 = input()
s2 = input()
s3 = ""


def fun(i, j, k, s):
    global s1
    global s2
    global s3
    if i == len(s1) or j == len(s2):
        if len(s3) == len(s):
            s3 = min(s, s3)
        elif len(s3) < len(s):
            s3 = s
        return k
    if s1[i] == s2[j]:
        return fun(i + 1, j + 1, k + 1, s + s1[i])
    return max(fun(i + 1, j, k, s), fun(i, j + 1, k, s))


fun(0, 0, 0, "")
print(s3)