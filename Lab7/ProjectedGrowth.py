import numpy as np

IV = float(input("Enter initial value: "))
GR = float(input("Enter the monthly growth rate: "))


values = np.arange(3) + 1
projected_value = IV * (1 + GR) ** values

print("Projected Value for First 3 Months: ", projected_value)
