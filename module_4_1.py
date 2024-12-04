from fake_math import dividi as fake_dividi
from true_math import dividi as true_dividi

result1 = fake_dividi(69, 3)
result2 = fake_dividi(3, 0)
result3 = true_dividi(49, 7)
result4 = true_dividi(15, 0)

print(result1)
print(result2)
print(result3)
print(result4)