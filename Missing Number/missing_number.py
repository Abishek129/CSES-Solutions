n = int(input())
nums = list(map(int, input().split()))
d = {}
for num in nums:
    d[num] = 1
for i in range(1, n+1):
    if i not in d:
        print(i)
        break
