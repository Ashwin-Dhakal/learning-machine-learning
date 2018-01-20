import numpy as np
from statistics import mean
import matplotlib.pyplot as plt
from matplotlib import style
import math

x=np.array([1,2,3,4,5,6])
y=np.array([4,7,6,5,8,9])

# def best_fit(x,y):
#     m = (mean(x) * mean(y) - mean(x * y))/((mean(x) ** 2) - (mean(x ** 2))

m = (mean(x) * mean(y) - mean(x * y)) / ((mean(x) ** 2) - (mean(x ** 2))

print m
#     b = mean(y) - mean(x)
#     return     m,b
# m,b= best_fit(x,y)
# regression_line = [m*som + for som in x]
# plt.plot(x, regression_line)
# plt.show()

