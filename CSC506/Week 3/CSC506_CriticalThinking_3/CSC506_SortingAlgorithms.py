def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
    return arr

def merge_sort(arr):
    def merge(left, right):
        i = 0
        j = 0
        final = []

        # Merge each array until one is empty
        while(i < len(left) and j < len(right)):
            if left[i] < right[j]:
                final.append(left[i])
                i +=1
            else:
                final.append(right[j])
                j+=1

        if i < (len(left)):
            # Add left over elements in left to the end of the array
            final.extend(left[i:]) 
        else:
            # Add left over elements in right to the end of the array
            final.extend(right[j:])
        return final

    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    leftmerge = merge_sort(left)  
    rightmerge = merge_sort(right)

    return merge(leftmerge, rightmerge) 