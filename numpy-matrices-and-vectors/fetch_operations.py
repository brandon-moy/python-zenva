import numpy as np

an_array = np.arange(0, 11)
print(an_array)

# can be [0:5] but Python will know it means start
first_five = an_array[:5]
print(first_five)

# same here that it can be [6:10] by Python will know to run to the end of the array
last_five = an_array[6:]
print(last_five)

# reverse an array with -1
first_five_reversed = an_array[4::-1]
print(first_five_reversed)

# by setting -2 as the start, it will start from 2 from the end of the array
final_two = an_array[-2:]
print(final_two)