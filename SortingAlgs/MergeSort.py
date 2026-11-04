from randList import get_list 


#user_input = input("Please enter a comma seperated list of whole numbers")
#user_input2 = input("Please enter a second list of the same format")
#listA = [int(x) for x in user_input.split(",")]
#listB = [int(y) for y in user_input2.split(",")]

def merge(left,right):
    i = 0   #tracking position in left split
    j = 0   #tracking position in right split
    result = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])

    return result
def merge_sort(A):
    if len(A) <= 1:
        return A        #the smallest list we want is a list of 1 element, dont want any empty sets
    else: 
        middle = len(A) // 2
        left_side = A[:middle]
        right_side = A[middle:]

        sorted_left = merge_sort(left_side)     #recursive call
        sorted_right = merge_sort(right_side)   #recursive call

        return merge(sorted_left, sorted_right) #returns bot sides sorted

# listA = [5,1,4,2,8,9,3]
# print(merge_sort(listA))

if __name__ == "__main__":
    numbers = get_list()
    sorted_numbers = merge_sort(numbers.copy())  
    print("First 10 sorted numbers:", sorted_numbers[:10])
    print("Correctly sorted:", sorted_numbers == sorted(numbers))
