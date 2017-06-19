import numpy as np
import matplotlib.pyplot as plt
angle = [-40, -20, 0, 20, 40, 60, 80]
dists = [61, 177.33, 296.33, 680.33, 651, 534.67, 24.67]

# I wrote this to see if degrees of 3 or 2 were better.
# This seems to prove degrees of 3 are better than 2.
# 2 seems to not approximate the angle as well as 3 does.
# Even though 2 is closer to getting 90 correct than 3 is, that's only because its arch is lazy.
# Especially, 2 manages to massively overshoot what 0 is, while 3 definitely approximates it.

result = np.polyfit(angle, dists, 3)  # degree of 3
result2 = np.polyfit(angle, dists, 2) # degree of 2
equation = np.poly1d(result)
equation2 = np.poly1d(result2)
print equation
print equation2

# Get values
angrange = np.arange(-40, 90)
vals = np.polyval(result, angrange)
vals2 = np.polyval(result2, angrange)
points, = plt.plot(angle, dists, label='Points')
d3fit, = plt.plot(angrange, vals, label='D3 Fit')
d2fit, = plt.plot(angrange, vals2, label='D2 Fit')
plt.legend(handles=[points,d3fit,d2fit])
plt.savefig('example.png')
