import pandas as pd
df=pd.read_csv('../Dataset/SalesTransactions.json', encoding='UTF-8',dtype='unicode',
               sep='\t')
print(df)   