import pandas as pd

df=pd.read_csv('pandas1.txt')
print(df)


#Series

a=[1,2,3]
series=pd.Series(a)
print(series)
name=pd.Series(a,index=[10,20,30])
print(name)

dataset={'Games':["vollyball","cricket","chess"],'type':["outdoor","outdoor","indoor"]}
data=pd.DataFrame(dataset)
print(data)
print(data.loc[0])

#head and tail

print(df.head(2))








import numpy as np
import pandas as pd

s=pd.Series([1,3,5,np.nan,6,8])
print(s)
print(s[0])
s1=pd.Series([1,3,5,6,8])
print(s1)

dates=pd.date_range("20130102",periods=6)
print(dates)

df=pd.DataFrame(np.random.randn(6,4),index=dates,columns=list("ABCD"))
print(df)

df2=pd.Dataframe({"A":1.0,"B":pd.Timestamp("20221014"),
                  "C":pd.Series(1,index=list(range(4)),dtype="float32"),
                  "D":pd.Categorical(["test","train","test","train"]),
                  "E":np.array([3]*4,dtype="int32"),
                  "F":"foo"})
print(df2)
print(df2.dtypes)

print(df.tail(2))
print("===========")
print(df.head(2))
print("===========")
print(df)


