def remove_duplicates(arr):
    if not arr:
        return []
    
    unique_idx = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[unique_idx]:
            unique_idx += 1
            arr[unique_idx] = arr[i]
    
    return arr[:unique_idx + 1]

arr1 = [2, 2, 2, 2, 2]
print(remove_duplicates(arr1))  

arr2 = [1, 2, 3, 4, 4, 4, 5, 5]
print(remove_duplicates(arr2)) 

