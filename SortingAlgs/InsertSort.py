from randList import get_list 

def insert(Mylist):
    
    for i in range(1, len(Mylist)):
        j = i -1
        key = Mylist[i]
        while j >= 0 and Mylist[j] >= key:
            Mylist[j +1] = Mylist[j]
            j -=1
        Mylist[j+1] = key
    return Mylist

#     print(Mylist)
# insert([2,5,1,6,8,4,9])

if __name__ == "__main__":
    numbers = get_list()
    sorted_numbers = insert(numbers.copy())  
    print("First 10 sorted numbers:", sorted_numbers[:10])
    print("Correctly sorted:", sorted_numbers == sorted(numbers))
