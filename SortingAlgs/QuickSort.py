def QuickSort(arr):
    if len(arr) <= 1 :
        return arr 
    pivot = arr[0]
    rest = arr[1:]
    pileA= []
    pileB = []
    for value in rest:
        if value < pivot:
            pileA.append(value)
        else:
            pileB.append(value)
    A_sorted = QuickSort(pileA)
    B_sorted = QuickSort(pileB)

    return (A_sorted + [pivot] + B_sorted)

    

print(QuickSort([2,1,6,4,8,5,9]))
