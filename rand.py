# rand.py (revised version)
import random

# Function to generate random numbers in a list
def random_array(arr):
    for i in range(len(arr)):
        arr[i] = random.randint(1, 20)  # Random integer between 1 and 20
    return arr
