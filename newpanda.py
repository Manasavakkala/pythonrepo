import pandas as pd
df=pd.read_csv("C:/Users/user719/PycharmProjects/pythonProject/pokemon_data.csv")
print(df)

df['HP']

df.sort_values(['Speed'],ascending=True)
df.sort_values(['Type 1','Speed'],ascending=[1,0])


