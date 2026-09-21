def Sel(planter):
    for i in range(0, len(planter)-1):
        minVal = i
        for j in range(i+1, len(planter)):
            if planter[j] < planter[minVal]:
                minVal = j
        planter[i], planter[minVal] = planter[minVal], planter[i]
    print(planter)

Sel([5,2,9,1,7])

