w=int(input())
for i in range(w):
    word = input()
    if len(word)>10:
        print(word[0]+str(len(word[:-2])) +word[-1])
    else:
        print(word)

#Link: https://codeforces.com/problemset/problem/71/A