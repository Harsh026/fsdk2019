import numpy as np
x = np.random.randint(5, 16, 40)
print("Original array:")
print(x)
print("Most frequent value in the above array:")
print(np.bincount(x).argmax())