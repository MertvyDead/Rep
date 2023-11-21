def find_max_recursive(arr, n):
    if n == 1:
        return arr[0]
    else:
        max_rest = find_max_recursive(arr, n-1)
        if max_rest > arr[n-1]:
            return max_rest
        else:
            return arr[n-1]
a = [12,1234,52,31,565,1]
x_element= find_max_recursive(a,(len(a)))
print(x_element)

def find_max_iterative(arr):
    max_element = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]
    return max_element
print(find_max_iterative(a))