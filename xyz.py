# import pandas as tushar
# s = tushar.Series([3, -5, 7, 4],  index=['a',  'b',  'c',  'd'])
# print(s)

# data = {'Country': ['Belgium',  'India',  'Brazil'],

# 'Capital': ['Brussels',  'New Delhi',  'Brasilia'],

# 'Population': [11190846, 1303171035, 207847528]} 

# df = tushar.DataFrame(data,columns=['Country',  'Capital',  'Population'])
# print(df)


# abc= tushar.read_csv('sampledata.csv', header=None, nrows=5)
# # df.to_csv('myDataFrame.csv')
# print(abc)


# xlsx = tushar.ExcelFile('sample100data.xls')
# # print(xlsx)
# df = tushar.read_excel(xlsx,  'sample100data')
# print(df)


# import pandas as pd
# Print the Pandas version
# print(pd.__version__)

# Create series with Pandas
# series = pd.Series(data = ['Geeks','for','geeks'],
#                    index = ['A','B','C'])
# print(series)


# data = {'Fruits': ['Mango', 'Apple', 'Banana', 'Orange','grapes','kiwi','watermelon','dragonfruite','litchi'],
#         'Quantity': [40, 20, 25, 10,40,50,60,70,100],
#         'Price': [80, 100, 50, 70,40,50,60,70,200],
#         'Rs': [50, 200, 500, 700,40,50,60,70,400]}

# # Create Pandas Dataframe with dictionary
# df = pd.DataFrame(data)


# Print first 5 rows
# print(df.tail())
# print(df.nlargest(2, 'Quantity'))
# print(df.nsmallest(2, 'Quantity'))
# Select the price > 50
# print(df[df.Price < 50])

# Select the FRUITS name
# print(df['Fruits'])


# df.rename(columns={'Fruits': 'FRUITS',
#                    'Quantity': 'QUANTITY',
#                    'Price': 'PRICE'},
#           inplace=True)
# print(df)

# print(pd.melt(df))


# Pivot table
# pivot = df.pivot(columns='FRUITS',
#                  values=['PRICE', 'QUANTITY'])
# print(pivot)


# Drop the DISCOUNT Columns
# df1 = df.drop(columns=['QUANTITY'], axis=1)
# print(df1)

# Drop 2nd and 4th rows
# df2 = df.drop([1, 3], axis=0)
# print(df2)


# print(df.sort_values('Price', ascending=False))
# print(df)

# xyz = df.dtypes
# print(xyz)
# print(df.shape)
# print(df.info())


# df['Quantity'] = df['Quantity'].astype('int32')
# df['Fruits'] = df['Fruits'].astype('str')
# df['Price'] = df['Price'].astype('float')

# print(df.info())
# print(df.values)

# # Sorting in Ascending order
# print(df.sort_values('Price', ascending=False))

# df.reset_index(drop=True, inplace=True)
# print(df)


# df.reset_index(drop=True, inplace=True)
# print(df)


# df.rename(columns={'Fruits': 'FRUITS',
#                    'Quantity': 'QUANTITY',
#                    'Price': 'PRICE'},
#           inplace=True)
# print(df)
