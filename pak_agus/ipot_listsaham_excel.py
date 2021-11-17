import pandas as pd

read_file = pd.read_excel('listsaham.xlsx')
listsaham = read_file['CODE'].tolist()
