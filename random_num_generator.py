import numpy as np

rand = np.random.randint(1, 50, 5000)

fd = open('input.txt', 'w')

for i in rand:
    fd.write(f"{i}\n")
