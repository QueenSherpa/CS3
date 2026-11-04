import random

LIST_SIZE = 1000
MIN_VALUE = 1
MAX_VALUE = 10000

SEED = 42

def _generate():
    rng = random.Random(SEED) 
    return [rng.randint(MIN_VALUE, MAX_VALUE) for _ in range(LIST_SIZE)]

_MASTER_LIST = _generate()

def get_list():
    return _MASTER_LIST.copy()

if __name__ == "__main__":
    numbers = get_list()
    print(f"Generated {len(numbers)} integers in the list.")
    print("First 20 integers in the list: ", numbers[:20])


