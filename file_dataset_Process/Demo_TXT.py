import pandas as pd
df=pd.read_csv('../Dataset/SalesTransactions.txt', encoding='UTF-8',dtype='unicode',
               sep='\t', low_memory= False)
print(df)