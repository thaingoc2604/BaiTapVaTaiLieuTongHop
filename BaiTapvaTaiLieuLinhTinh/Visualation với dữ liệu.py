import matplotlib.pyplot as plt
import numpy as np
days = list(range(1,9))
celsius_values = [25.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1]
#Ta dùng chuỗi ‘--r’ để vẽ line graph, và ‘sr’ để vẽ các điểm rời rạc.
days = list(range(1,9))
celsius_values=[25.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1]
print(plt.plot(days, celsius_values,'--r'))
print(plt.plot(days,celsius_values, 'sr'))
#plt.plot(days,celsius_values,color = 'r', ls = '--', marker='s', lw = 5, markeredgewidth = 10)
################
days = list(range(1,9))
celsius_min = [19.6, 24.1, 26.7, 28.3, 27.5, 30.5, 32.8, 33.1]
celsius_max = [24.8, 28.9, 31.3, 33.0, 34.9, 35.6, 38.4, 39.2]
celsilus_avg =list(map(lambda x: np.average(x),zip(celsius_min,celsius_max)))
#plt.plot(days,celsius_min,"b--s",days,celsius_max,"r--s")
#
X = [ (4,2,1),(4,2,2), (4,2,3), (4,2,5), (4,2,(4,6)), (4,1,4) ]
print(plt.subplots_adjust(bottom=0.974, left=0.05, top = 0.975, right=0.95))

for nrows, ncols, plot_number in X:
	print(plt.subplot(nrows, ncols, plot_number))

print(plt.show())
