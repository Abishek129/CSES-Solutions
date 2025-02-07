n = int(input())
nums= input().split(" ")
stack = [int(nums[0])]
for i in range(1, n):
    
    if int(nums[i]) >= stack[-1]:
        stack.append(int(nums[i]))
        continue
    
    target = int(nums[i])
    if target < stack[0]:
        stack[0] = target
        continue
    left = 0
    right = len(stack)-1
    while (left <= right):
        mid = (left + right)//2
        if target >= stack[mid]:
            left = mid + 1
        else:
            right = mid - 1

    stack[left] = target

print(len(stack))
