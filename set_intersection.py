
n1 = int(input())
set1 = set(input().split())

n2= int(input())
set2 = set(input().split())

set3 = set2.intersection(set1)

print(len(set3))
