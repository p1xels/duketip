import numpy as np
angle = [-40, -20, 0, 20, 40, 60, 80]
dists = [61, 177.33, 296.33, 680.33, 651, 534.67, 24.67]

result = np.polyfit(angle, dists, 3)  # degree of 3
equation = np.poly1d(result)

print equation

try:
    x = int(raw_input("Angle: "))
except ValueError:
    print "Not a number?"

print "%d: %f" % (x, equation(x))