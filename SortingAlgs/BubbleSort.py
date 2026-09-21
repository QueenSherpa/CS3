user_input = input("Please enter a comma seperated list of numbers ")
population = [int(x) for x in user_input.split(",")]

def bubbleSort(population):
    for i in range(0, len(population) - 1):
        done = True
        for j in range(0, len(population) -i -1):
            if population[j] > population[j+1]:
                population[j], population[j+1] = population[j+1], population[j]
                done = False
        if done:
            return
bubbleSort(population)
print(population)

    
