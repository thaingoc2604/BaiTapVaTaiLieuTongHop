import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#minh họa series:
S=pd.Series(np.random.randint(100,size=5))
print(S)
# nd array trong Series:
phone=['iPhone',"Samsum Note","Samsum S","Nokia"]
quantities=[10,60,37,40]
S=pd.Series(quantities,index=phone)
print(S)
print("*"*30)
# Cộng Và Trừ hai Series:
phone=['iPhone',"Samsum Note","Samsum S","Nokia"]
quantities=[10,3,5,40]
S1=pd.Series(quantities,index=phone)
S2=pd.Series([30,-10,10,0],index=phone)
print(S1+S2)
print("*"*30)
S3=pd.Series([0,41,60,15],index=phone)
print(S2+S3)
#Trừ thì làm tương tự cộng vậy đó nha:
print("*"*30)
# có thễ truy xuất giá trị Đơn của q hoặc nhiều giá trị của Series qua chỉ số hoặc 1 list của số:
print("chỉ số index của Samsum Note Trong Series của S là:",S["Samsum Note"])
print("chỉ số index của Samsum Note Trong Series của S2 là:",S2["Samsum Note"] )
print("chỉ số index của Samsum Note Trong Series của S3 là:",S3["Samsum Note"])

#thay vì phải truyền vào gồm hai danh sách như trên thì ta có thể tạo Series bằng cách truyền 1 dictionary
phones=['iPhone',"Samsum Note","Samsum S","Nokia"]
quantities=[10,15,16,17]
dictionary=dict(zip(phones,quantities))
print(dictionary)

#TẠO 1 PANDAS SERIES:
phones=['iPhone',"Samsum Note","Samsum S","Nokia","Realmi"]
quantities=[10,5,2,7,9]
sales=dict(zip(phones,quantities))
S=pd.Series(sales)
print(S)
print("*"*30)
#THAO TÁC TOÁN HỌC VỚI PANDAS: 
print(S)
print("phép toán bình phương:\n",S**2)
print("phép toán nhân\n",S*2)
print("phép toán cộng\n",S+15)
print("S*(S*S)\n",(S*(S*S)))
print(S.dtype)
print(S.empty)
print(S.ndim)
print(S.size)
print(S.values)
print("Trả về hàng đầu tiên là:\n",S.head(1))
print("Trả về hàng cuối cùng là:\n",S.tail(1))

#PHƯƠNG THỨC APPLY:
print(S.apply(np.cos))
print("*"*30)
print(S)
T=S.apply(lambda x:x if x%5==0 else x**3)
print(T)
print("<->"*50)
#DATA FRAME:
#1. CÁCH TẠO 1 DATA_FRAME RỖNG:
df=pd.DataFrame()
print(df)
#2. TẠO 1 DATA_FRAME TỪ 1 LIST
lst_df=["stantos","france","spain"]
df=pd.DataFrame(lst_df)
print(df)
#2.1
lst_df1=[["stantos",15],["france",24],["spain",36]]
df=pd.DataFrame(lst_df1)
print(df)
# TẠO 1 DATA FRAME TỪ 1 DICTIONARY CỦA 1 LIST HOẶC ADARAY
T_T={"year":[1990,1995,1997,2000],"Population":[147562778,951765489,331116545,107023014],"Total":[369410,525354,152364,897615],"Violent":[1475,6589,2205,3369]}
TT_df=pd.DataFrame(T_T)
print(TT_df)
# Tạo 1 data_Frame từ list của dictionary
data=[{"C++":500,"C#":400,"Java":300},{"C++":1,"C#":2,"Java":200}]
data_df=pd.DataFrame(data,index=['NameStudents',"ClassStudebts"])
print(data_df)

#Tạo data frame từ dict của dictionary:
print("----------Tạo data frame từ dict của dictionary:----------")
data={"one":pd.Series([1,4,5],index=[1,2,3]),"Two":pd.Series([1000,5474,1101,5555],index=[1,2,3,4])}
df=pd.DataFrame(data)
print(df)
# Copy=False:
share_df=pd.DataFrame(df)
share_df['Four']=pd.Series(["C++","C#","Java"])
print(df)
# Copy=True:
print("+"*50)
new_df=pd.DataFrame(df,copy=True)
new_df['three']=pd.Series(["C++","C#","Java"])
print(df)
print(new_df)
print("---------------------------- Tiếp------------------------")
T_T={"year":[1990,1995,1997,2000],"Population":[147562778,951765489,331116545,107023014],"Total":[369410,525354,152364,897615],"Violent":[1475,6589,2205,3369]}
TT_df=pd.DataFrame(T_T)
print(TT_df)
#print("----------sử dụng các hàng của data frame:-------------"
Vi_Tri=["một","hai","ba","bốn"]
TT_df=pd.DataFrame(T_T,index=Vi_Tri)
print(TT_df)
#print("----------sử dụng các cột của data frame để làm các chỉ số index:-----------")
TT_df=pd.DataFrame(T_T,columns=["Population","year","Violent"],index=T_T["Total"])
print(TT_df)
print("-"*60)
#print("----------sử dụng lệnh set.index để biến cột thành các chỉ mục:----------")
TT_df=pd.DataFrame(T_T,columns=["Population","year","Total","Violent"])
new_TT_df=TT_df.set_index("Violent",inplace=True)
print(new_TT_df)
print("*"*60)
print("---- Selecting(Chọn)----setting(Gán)----deleting(Xóa)----")
T_T={"year":[1990,1995,1997,2000],"Population":[147562778,951765489,331116545,107023014],"Total":[369410,525354,152364,897615],"Violent":[1475,6589,2205,3369]}
TT_df=pd.DataFrame(T_T)
print(TT_df)
# Chọn Selecting:
# cách 1:
print(TT_df["year"])
#cách 2:
print(TT_df.year)
# Gán setting:
vio=pd.Series([14,55,79,41],index=(TT_df.index))
print(vio)
TT_df["Violent"]=vio
print(TT_df)
#thêm một cột mới nha:
TT_df['Mueder']=np.nan
print(TT_df)
TT_df['Murder']=9119
print(TT_df)
#cách 2 của phần thêm 1 cột mới:
TT_df=pd.DataFrame(T_T,columns=["year","Violent","Total","Population","NEW"])
print(TT_df)
#chỉ định chính xác :
murder=[5478,6985,3225,4171]
TT_df['Murder']=murder
print(TT_df)
# -----------------XÓA----------------------
print(TT_df)
del TT_df['NEW']
print(TT_df)
print(" -----Tính Tổng Và Tổng Tích Lũy--------")
print(TT_df['Murder'].sum())
print("--------------Chuyển vị transpose--------------")
#tức là chuyển cột thành hàng và ngược lại :
print(TT_df.T)

#-------------------Tạo 1 Panel rỗng------------------:
print("*"*50)
print("--------------GIỚI  THIỆU VỀ PANLE-------------")
#print("------Tạo 1 Panel rỗng--------")
#p=pd.Panel()
'''data=np.random.rand(2,3,4)
p=pd.Panel(data)
print(p)'''
print("------- .loc---.iloc----.ix-----")
#đầu tiên ta tạo 1 data frame để minh họa phần này nha :
T_T={"year":[1990,1995,1997,2000,2002],"Population":[147562778,951765489,331116545,107023014,158757697],"Total":[369410,698462,525354,152364,897615],"Violent":[1475,6589,1546,2205,3369]}
TT_df=pd.DataFrame(T_T)
print(TT_df)
print("select row having row numbers is 1")
print(TT_df.iloc[1])
print(TT_df.loc[1])
print(TT_df.iloc[3,2])
# Trường hợp này ta sử dụng .iloc hay .loc đều cho 1 kết quả vì index tạo mặc định cũng là row numbers:
# ta chứng sẽ chứng minh .iloc không làm việc với nhãn bằng cách chỉnh lại nhãn:
Vi_T=["một","hai","ba","bốn","năm"]
TT_df=pd.DataFrame(T_T,index=Vi_T)
print(TT_df)
# khi run thì nó sẽ không chạy đc do .iloc không làm việc với nhãn
#print(TT_df.iloc["một"])
# Nhưng khi ta sử dụng .loc thì nó chay đc do .loc làm việc đc với nhãn:
print(TT_df.loc["một"])
# và ta cũng không thể dùng row number khi dùng .loc:
#print(TT_df.loc[0])
print("*"*30)
# bằng cách này ta có thể lọc hàng theo 1 điều kiện nào đó:--nhưng điều này không thể thực hiện với .iloc<--
print(TT_df.loc[TT_df.year>1995])

# nhưng với .ix thì ta có thể làm tất cả các điều của .iloc và .loc mà không bị phát sinh lỗi :
# đầu tiên thì ix làm việc đc với nhãn còn .iloc thì không:
# tôi  sẽ không giói thiệu về .ix trong bài này
# lọc lấy cột và hàng theo ý nuốn của bạn:
print("_----------------")
print(TT_df.iloc[[0,4],[1,3]])
# lọc theo nhãn dùng .loc
print(TT_df.loc[["một","hai"],["year","Total"]])
# kĩ thuật slicing  với hàng
print(TT_df[0:2])
print("----Đọc dữ liệu-----")
df=pd.read_csv("sales_14.csv",header=0,index_col='Date',parse_dates=True)
print(df.head(6))

print("---- đọc dữ liệu và kĩ thuật reindexing-------")
# kĩ thuật ReinDexing:
q_sale_2016=pd.DataFrame({'turnover':[1200,1300,1400,1500]},index=['Apr','Jul','Jan',"Oct"])
print(q_sale_2016)
q_sale_2017=pd.DataFrame({'turnover':[1100,1500,1300,1200]},index=['Jan','Apr','Jul',"Oct"])
print(q_sale_2017)
# index cần tuân theo thứ tự thời gian:
oder=["Jan","Apr","Jul","Oct"]
print(q_sale_2016.reindex(oder))
print(q_sale_2017.sort_index())
print("-----")
# nó sẽ in ra kết qua theo index của q_sale_2017 nhưng các giá trị thì tương ứng theo turnover của q_sale_2016 
#cụ thể là: ta thấy nó sẽ gán các index bằng các giá trị turnover của q_sale_2016 và sau đó nó sẽ in các index đó theo thứ tự của
# trong index của q_sale_2017  
print(q_sale_2016.reindex(q_sale_2017.index))
# Lọc dữ liệu trong pandas:
print("-------Lọc dữ liệu trong pandas----------")
# lệnh .Where() 
s=pd.Series([12,34,56,78],index=[1,2,3,4])
print(s)
# kiểm tra xem tát cả các phần tử có lớn hơn 50
print(s>50)
# in ra các phần tử lớn hơn 50:
print(s[s>50])
# sử dụng phương thức .where()
print(s.where(s>50))
# mảng ngẫu nhiên các số theo phân phối chuẩn (chữ n ở cuối là viết tắt của normal)
df=pd.DataFrame(np.random.randn(5,4)*100,columns=list("ABCD"))
print(df)
print(df[df>0])
print(df.where(df>0,-df))
# .query
df=pd.DataFrame(np.random.randint(100,size=(10,3)),columns=list('abc'))
print(df)
print(df[(df.a<df.b)&(df.b<df.c)])
print("cách này tương đương khi làm với query")
print(df.query('a<b and b<c'))

# toán tử in và not in trong query:
df=pd.DataFrame({"a":list('aabbccddeeff'),"b":list('aaaabbbbcccc'),"c":np.random.randint(5,size=12),"d":np.random.randint(9,size=12)})
print(df)
	# toán tử in
print(df.query('a in b'))
# cách tương tự với in ta dùng isin
print(df[df.a.isin(df.b)])
#not in
print("----- not in------------")
print(df.query('a not in b'))
# cách tương tự với isin ta dùng ~isin:
print(df[~df.a.isin(df.b)])
# phương thức get():
print(df.get('s',[1,2,3,4]))
# .SELCT(FUNCTION AXIS=0)
#print(df.select(lambda x: x!='b',asix=1))
print("*"*30)
lookup=pd.DataFrame(np.random.rand(20,4),columns=['A','B','C','D'])
print(lookup)
# trích q tập hợp các hàng và cộng 
print(lookup.lookup(list(range(0,10,2)),['B','C','A','B','D']))

# Xử lí missing data (NaN)
# từ dòng 259 --> 268 là ta đang tạo ra 1 Series có giá trị NaN (not a number)
phone=['iPhone',"Samsum Note","Samsum S","Nokia"]
quantities=[10,20,30,100]
sales=dict(zip(phone,quantities))
S=pd.Series(sales)
brands=["iPhone","Samsum Note","Samsum S","Nokia","LG","HTC"]
SS=pd.Series(sales,index=brands)
print(SS)
# ví dụ tạo ra Series có NaN:
d={"a":23,"b":45,"c":None,"d":0}
print(pd.Series(d))
# từ dòng 270--> 272 là ta dang tạo ra 1 DataFrame có giá trị NaN(not a number)
df=pd.DataFrame(np.random.randn(5,4)*100,columns=list("ABCD"))
print(df)
print(df[df>0])
 #phương thức isnull() và notnull() kiểm tra phần tử có là NaN hay không
print(SS)
print("------")
# là NaN
print(SS.isnull())
# không phải NaN
print(SS.notnull())
# kiểm tra từng phần tử coi nó có NaN không
dff=df[df>0]
print(dff)
print(dff['A'].isnull())
print(dff['A'].notnull())
# Loại bỏ tất cả các phần tử  là NaN trong Series SS:
# in ra Series trước khi xóa NaN:
print(SS)
# in ra Series Sau khi Xóa NaN:
print(SS.dropna())
# Loại bỏ tất cả các phần tử  là NaN trong Series dff:
print(dff,"\n")
print(dff.dropna())
 # gán gái trị mặc định cho missing data:
print(SS.fillna(10000))
#3################
print("*"*30)
print(dff)
print("bfill")
print(df.fillna(method='bfill'))
print("ffill")
print(df.fillna(method='ffill'))
# Tổ chức lại bảng dữ liệu:
# .pivot là thuộc dạng multi-level index
df = pd.DataFrame([[2011,'Iphone',10000],[2011,'SS',30000],[2011,'LG',123000],
[2012,'SS',134500],[2012,'LG',90000],[2012,'Iphone',23400],[2013,'Iphone',56000],
[2013,'LG',234000],[2013,'SS',1234567]], columns=['year','product','turnover'])
print(df)
# index là cột lề bên trái đi xuống á; columns là các cột dọc xuống
print(df.pivot(index='year',columns='product',values='turnover'))
#############################
print(df.set_index(['year','product'],inplace=False))
#.unstack() và .stack()
#thuộc dạng multi-level index
print(df)
# TA CHƯA LÀM ĐC HÀM .UNSTACK()
#print(df.unstack(level='turnover'))
df=df.set_index(['product','year'])
print(df)
# Cần hóa đổi vị của hai index level là year và product :
print(df.swaplevel(0,1))
print(df.swaplevel("year","product").sort_index())
# Tổ Chức Lại Dữ Liệu:
df = pd.DataFrame([[2011,'Iphone',10000],[2011,'SS',30000],[2011,'LG',123000],
[2012,'SS',134500],[2012,'LG',90000],[2012,'Iphone',23400],[2013,'Iphone',56000],
[2013,'LG',234000],[2013,'SS',1234567]], columns=['year','product','turnover'])
print(df)
df1=df.pivot(index='year',columns='product',values='turnover').reset_index()
print(df1)
# Câu hỏi đặt ra là làm thế nào để chuyễn từ dạng 2 sang dạng 1:
#pandas.melt(frame, id_vars=None, value_vars=None, var_name=None,value_name='value', col_level=None)
print(df)
print("----------")
# dòng 334 sẽ chuyễn mọi cột thành hàng:
print(pd.melt(df))
# 
print(pd.melt(df,id_vars=['year'],var_name='product',value_name='turnover'))

# Pivot Table:
df=pd.read_csv("sales-funnel.csv",sep=',')
print(df)
print(df[:0])
print(df.pivot_table(index='Manager',columns='Rep',values ='Price',margins='True'))
# Nhóm dữ liệu:
# groupby:
dfGb=pd.DataFrame({'A':['foo','bar','foo','bar'],'B':['one','one','two','three'],'C':np.random.randn(4),'D':np.random.randn(4)})
print(dfGb)
grouped=dfGb.groupby(['A','B'])
print(grouped.last())
# đếm số lượng nhóm:
print(grouped.count())
# tính tổng:
print(grouped.sum())
print(dfGb.A.unique())
print(dfGb.B.unique())
# groupby trong Series:
print("-"*50)
s=pd.Series(list(dfGb['C']),dfGb['A'])
print(s)
grouped=s.groupby(level=0)
print(grouped.first())
print(grouped.count())
# grouped.1 cái phương thức nào đó có nghĩa là nó sẽ nó sẽ thực hiện 1 phương thức đó trong dữ liệu của trong cái Series 
# hay DataFrame rồi nó sẽ in ra kết quả đc tổ chức theo 1 cấu trúc dữ liệu nào đó: 
print(grouped.sum())

#######################################
#các keys được sắp xếp trong quá trình groupby
print(dfGb.groupby(['A','B']).sum())
# các keys không được sắp xếp trong quá trình groupby
print(dfGb.groupby(['A','B'],sort=False).sum())
# ta nhận đc kết quả groupby bằng kiểu dictionary thông qua thuộc tính groups
print(dfGb.groupby('A').groups)
print("-"*50)
# cách duyệt qua toàn bộ grouped:
print(dfGb)
print(grouped.last())
grouped=dfGb.groupby(['A','B'])
for name,group in grouped:
	print(name)
	print(group)
# phương thức get_group() giúp ta có đc giá trị của 1 nhóm:
print("-"*50)
print(grouped.get_group(('bar','three')))
#aggregation:
print("------------aggregation----------")
dfGb=pd.DataFrame({'A':['foo','bar','foo','bar'],'B':['one','one','two','three'],'C':np.random.randn(4),'D':np.random.randn(4)})
print(dfGb)
print(grouped.aggregate(np.sum))
# trong quá trình aggregate() ta có thể cùng một lúc áp dụng nhiều hàm:
print(grouped['D'].aggregate([np.sum,np.mean,np.std]))
print(dfGb['D'].aggregate([np.sum]))
print(dfGb['D'].aggregate([np.mean]))
print(dfGb['D'].aggregate([np.std]))

# ta có thể áp dụng từng hàm cho từng cột trong quá trình aggregate:
print(grouped.agg({'C':np.sum,'D':np.mean}))
# nhóm dữ liệu phần 2:
# chuyển đổi Transformation:
np.random.seed(1234)
index = pd.date_range('10/1/1999', periods=1100)
ts = pd.Series(np.random.normal(0.5, 2, 1100), index)
ts = ts.rolling(window=100,min_periods=100).mean().dropna()
# kiễm tra dử liệu có phải kiểu datatime64 không
print(ts.head())
print(ts.tail())
print(ts.index)
# tiến hành chuẩn hóa dữ liệu transformation:
key = lambda x: x.year
year_grouped= ts.groupby(key)
zscore = lambda x: (x - x.mean()) / x.std()
transformed = year_grouped.transform(zscore)
# xem kết qua trước khi transformation:
print("Original Data")
print(year_grouped.mean())
print(year_grouped.std())
# kết quả sau khi transformation
print ("Transformed Data")
grouped_trans = transformed.groupby(key)
print(grouped_trans.mean())
print(grouped_trans.std())
# bước cuối cùng là vusualingzing dữ liệu:
compare = pd.DataFrame({'Original': ts, 'Transformed': transformed})
print(compare.plot())
#plt.show()
# sự khác biệt giữa apply() và transform()
'''dfGb=pd.DataFrame({'A':['foo','bar','foo','bar','foo','bar','foo','foo'],'B':['one','one','two','three','two', 'two', 'one', 'three'],
	'C':np.random.randn(8),'D':np.random.randn(8)})
print(dfGb)
print(df.groupby('A').apply(lambda x: (x['C'] - x['D'])))'''
print("-----------------Filterration--------------")
# index_col là lấy cột đó ra làm index:
sales=pd.read_csv('sales_14.csv',sep=',',index_col=0)
print(sales)
#Yêu cầu: Sau khi thực hiện groupby theo ‘Company’ cần loại bỏ tất cả các hàng mà có tổng 
#trên ‘Units’ nhỏ hơn hoặc bằng 35
print(sales.groupby('Company').filter(lambda g:g['Units'].sum() > 35))
print("-----------------Tính Đoán số học-------------")
exchange=pd.read_csv('Exchangerates.csv')
# head(n): in ra n hàng
print(exchange.head())
# values= n : n đó là giá trị mà mình sẽ in ra:vd như values=Value hoặc values=SUBJECT ...vv.v
# [['AUS','KOR']] nó sẽ lấy ra hai phần tử KOR và AUS của cột LOCATION:
exchange = exchange.pivot(index='TIME',columns='LOCATION',values='Value') [['AUS','KOR']]
print(exchange.head())
# Kĩ thuật broadcasting khi thực hiên các phép toán học
print("--->Kĩ thuật broadcasting khi thực hiên các phép toán học<---")
print((exchange / 2).head())
print((exchange**0.5).head())
print((exchange/exchange['KOR']).head())
print(exchange.divide(exchange['KOR'],axis=0).head())
# sử dụng các phương thức
# phương thức pct_change() để tính toán thay đổi % theo thời gian:
print(exchange.pct_change()*100)
print("--->time Series<---")
from datetime import datetime, timedelta as delta
# ndays=n với n phải bằng số phần tử trong values:
ndays = 11
# datatime(ngày,tháng,năm) là thời gian bắt đầu:
start = datetime(2017, 3, 31)
dates = [start - delta(days=x) for x in range(0, ndays)]
values = [25, 50, 15, 67, 70, 9, 28, 30, 32, 12,17]
ts = pd.Series(values, index=dates)
print(ts)
sales = pd.read_csv("sales_14.csv",header=0, index_col='Date', parse_dates=True)
print(sales.head())
# ba Cách này đều là 1:
print(sales.loc['2015-02-11',:])
print(sales.loc['2015-Feb-11',:])
print(sales.loc['2015-11-February',:])
# lấy ra 2 phần tử đầu tiên trong dữ liệu:
print(sales.loc['2015-02',:].head(2))
#Converting to Timestamps chuyển đỗi 1 đối tượng
print(pd.to_datetime(pd.Series(['Jul 31, 2009', '2010-01-10', None])))
print(pd.to_datetime(['2005/11/23', '2010.12.31']))
print(pd.DataFrame({'year': [2015, 2016],'month': [2, 3],'day': [4, 5],'hour': [2, 3],}))
print(sales.resample('W')['Units'].ffill())
print(sales.resample('W')['Units'].sum())
############# 
print(sales.reset_index(inplace=True))
print(sales.Date.dt.hour)
print(sales.head())