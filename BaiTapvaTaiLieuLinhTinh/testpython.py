'''import datetime
dt = datetime.datetime.strptime("2016-04-15T08:27:18-0500", "%Y-%m-%dT%H:%M:%S%z")
print(dt)
import dateutil.parser
dt = dateutil.parser.parse("2016-04-15T08:27:18-0500")
print(dt)
from datetime import datetime, timedelta, timezone
JST = timezone(timedelta(hours=+9))
dt = datetime(2015, 1, 1, 12, 0, 0, tzinfo=JST)
print(dt)
%load_ext line_profiler'''
#%%file mprun_demo.py
def insertion_sort(list_a):
	index_length=range(1,len(list_a))
	for i in index_length:
		value_to_sort=list_a[i]

		while list_a[i-1]>value_to_sort and i>0:
			list_a[i],list_a[i-1]=list_a[i-1],list_a[i]
			i=i-1
	return list_a

print(insertion_sort([13,4,5,8,69,7,3,4,4]))
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 5, 50)
print(x)
y = np.linspace(0, 5, 50)[:, np.newaxis]
print(y)
z = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)
plt.imshow(z, origin='lower', extent=[0, 5, 0, 5], cmap='viridis')

plt.colorbar()
#np.random.seed(42)

x = np.random.randn(100)
bins = np.linspace(-5, 5, 20)
counts = np.zeros_like(bins)
i = np.searchsorted(bins, x)

np.add.at(counts, i, 1)
plt.plot(bins, counts, linestyle='steps')
#plt.show()
import matplotlib.pyplot as plt
import numpy as np
plt.figure()
plt.subplot(2, 1, 1) # (rows, columns, panel number)
plt.plot(x, np.sin(x))
# create the second panel and set current axis
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x))
plt.show()
