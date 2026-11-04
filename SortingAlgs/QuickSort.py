from randList import get_list


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

    

# print(QuickSort([2,1,6,4,8,5,9]))

if __name__ == "__main__":
    numbers = get_list()
    sorted_numbers = QuickSort(numbers.copy())  
    print("First 10 sorted numbers:", sorted_numbers[:10])
    print("Correctly sorted:", sorted_numbers == sorted(numbers))
