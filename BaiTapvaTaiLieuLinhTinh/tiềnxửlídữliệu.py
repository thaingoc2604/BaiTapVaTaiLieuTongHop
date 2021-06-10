import sklearn as preprocessing
#from sklearn import preprocessing

int_data=np.array([

	[2.1,-1.9,5.5],
	[-1.5,-2.4,3.5],
	[0.5,-7.9,5.6],
	[5.9,2.3,-5.8]
])
# Binarization
binarization_data=preprocessing.Binarizer(threshold=0.5).fit_transform(int_data)
print(int_data)
print(binarization_data)
#2 mean removal
# tinh mean(trung bình) std(độ lệch)
mean=int_data.mean(axis=0)
std=int_data.