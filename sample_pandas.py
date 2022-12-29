import pandas as pd
df=pd.read_csv("C:/Users/user719/PycharmProjects/pythonProject/pokemon_data.csv")
print(df)

df.columns

#Read each Column

print(df[['Name','Type 1', 'HP']])

#Read each row

print(df.iloc[0:4])

for index,row in df.iterrows():
    print(index,row)


print(df.iloc[3,5])

print(df.iloc[2,1])

df.sort_values(['Speed'],ascending=True)


df.sort_values(['Type 1', 'Speed'], ascending=[1, 0])

#drop a column from df







