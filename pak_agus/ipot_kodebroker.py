import pandas as pd

read_file = pd.read_excel('kodebroker.xlsx')
kodebroker = read_file['CODE'].tolist()
