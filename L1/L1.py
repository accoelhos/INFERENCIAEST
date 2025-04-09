import scipy
from scipy.stats import norm

#5.5
#a)
print(norm.cdf(1.04))
#b)
print(norm.cdf(-1.5))

#c)
z1 = 1
z2 = 2

area = norm.cdf(z2) - norm.cdf(z1)

print(f"A área entre z = {z1} e z = {z2} é aproximadamente {area:.4f}")
