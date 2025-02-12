import heapq

def merge_k_sorted_arrays(arrays):
    min_heap = []
    
    
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(min_heap, (arr[0], i, 0))  
    
    merged_array = []
    
    while min_heap:
        value, arr_idx, elem_idx = heapq.heappop(min_heap)
        merged_array.append(value)
        
        if elem_idx + 1 < len(arrays[arr_idx]):
            heapq.heappush(min_heap, (arrays[arr_idx][elem_idx + 1], arr_idx, elem_idx + 1))
    
    return merged_array


arrays = [
    [1, 3, 5, 7],
    [2, 4, 6, 8],
    [0, 9, 10, 11]
]
print(merge_k_sorted_arrays(arrays))