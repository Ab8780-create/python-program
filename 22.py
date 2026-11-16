# 1. Import complete module
import math
print(math.sqrt(25))

# 2. Import specific function
from math import factorial
print(factorial(5))

# 3. Import multiple functions
from math import pow, ceil
print(pow(2, 3))
print(ceil(4.2))

# 4. Import with alias
import math as m
print(m.pi)