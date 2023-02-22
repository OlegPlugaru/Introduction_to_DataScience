import mpmath

mpmath.mp.dps = 100000
pi_str = str(mpmath.pi)

print(pi_str)
print(len(pi_str))
