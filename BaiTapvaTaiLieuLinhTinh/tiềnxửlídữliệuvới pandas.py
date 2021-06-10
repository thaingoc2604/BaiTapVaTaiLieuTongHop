import pandas as pd
import numpy as np
S=pd.Series(np.random.randint(100,size=5))
print(S)
print(S.index)
print(S.values)
phone=['Iphone',"samsum note","samsum S","nokia"]
quantities=[10,12,30,100]
diction=dict(zip(phone,quantities))
print(diction)
S=pd.Series(diction)
print(S)
# tạo DataFrame
df=pd.DataFrame([["Phương",2000,1],["Thái",2018,2],["Ngọc",2020,3]])
print(df)
# tạo 1 DataFrame từ 1 dictionary của 1 list
dict_tion={"Phương":[11,12,13,14,15],"Thái":[25,10,26,14,00],"Ngọc":[17,18,19,20,21]}
df=pd.DataFrame(dict_tion,index=["Ngọc","Thái","Phương","Yasuo","Vayne"])
print(df)
df2=pd.DataFrame({'month':[1,4,7,10],
	'year':[2012,2014,2013,2014],'sale':[55,40,84,31]})
print(df2)
print(df2.set_index('month','sale'))