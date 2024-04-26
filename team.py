n=int(input())
counter=0
for i in range(n):
    l = list(map(int, input().split()))
    if l.count(1)>=2:
        counter=counter+1
print(counter)