from randList import get_list

numbers = get_list()   # this file's own copy of the 1,000 integers



# user_input = input("Please enter a comma seperated list of numbers ")
# population = [int(x) for x in user_input.split(",")]

def bubbleSort(population):
    for i in range(0, len(population) - 1):
        done = True
        for j in range(0, len(population) -i -1):
            if population[j] > population[j+1]:
                population[j], population[j+1] = population[j+1], population[j]
                done = False
        if done:
            break
    return population
# bubbleSort(population)
# print(population)

if __name__ == "__main__":
    numbers = get_list()
    sorted_numbers = bubbleSort(numbers.copy())  
    print("First 10 sorted numbers:", sorted_numbers[:10])
    print("Correctly sorted:", sorted_numbers == sorted(numbers))
