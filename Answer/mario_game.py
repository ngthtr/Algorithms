
N = input()
arr = input().split()
for i in range(len(arr)):
    arr[i] = int (arr[i])
# arr = [7,2,1,8,4,3,5,6]


result = 0

min = 0
max = 0
dimension = "up"
for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        if dimension != "down":
            max = arr[i]
            result += max
            dimension = "down"

    if arr[i] < arr[i+1]:
        if dimension != "up":
            min = arr[i]
            result -= min
            dimension = "up"
    # print("i = %s, dimension = %s, min = %s, max = %s, result = %s" % (i, dimension, min, max, result))
            
if dimension == "up":
    result += arr[len(arr) - 1]


print(result)
        






