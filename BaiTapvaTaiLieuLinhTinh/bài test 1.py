import numpy as np
import pandas as pd
phone=['iPhone',"Samsum Note","Samsum S","Nokia"]
quantities=[10,60,37,40]
S=pd.Series(quantities,index=phone)
print(S)
print("giá trị ",S[0:1])
# khởi tạo từ 1 dictionary:
phones=['iPhone',"Samsum Note","Samsum S","Nokia","Realmi"]
quantities=[10,5,2,7,9]
sales=dict(zip(phones,quantities))
S=pd.Series(sales)
print(S)
# tạo 1 data frame()
lst=["Phương","Thái","Ngọc"]
df=pd.DataFrame(lst)
print(df)
data={"One":pd.Series([15,36,51],index=[1,2,3]),"Two":pd.Series([55,19,23,78],index=[1,2,3,4])}
df=pd.DataFrame(data)
print(df)
print(df[0:1])