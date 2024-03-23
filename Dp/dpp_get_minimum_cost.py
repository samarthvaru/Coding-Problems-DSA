def getMinimumCost(arr):
    n = len(arr)
    min_cost = float('inf')

    for i in range(1, n):
        left = arr[i - 1]
        right = arr[i]
        new_num = (left + right) // 2  # Insert the integer between left and right
        arr.insert(i, new_num)  # Insert the new integer in the array
        cost = 0

        for j in range(1, len(arr)):
            cost += (arr[j] - arr[j - 1]) ** 2

        min_cost = min(min_cost, cost)
        arr.pop(i)  # Remove the inserted integer to try the next position

    return min_cost

if __name__ == '__main__':
    arr_count = int(input().strip())
    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = getMinimumCost(arr)
    print(result)
