def insert(Mylist):
    
    for i in range(1, len(Mylist)):
        j = i -1
        key = Mylist[i]
        while j >= 0 and Mylist[j] >= key:
            Mylist[j +1] = Mylist[j]
            j -=1
            Mylist[j+1] = key

            
    print(Mylist)
insert([2,5,1,6,8,4,9])

