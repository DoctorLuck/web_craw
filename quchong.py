import pandas as pd

csvfile='GetUser.csv'
file=pd.read_csv(csvfile,header=0)
dateList=file.drop_duplicates()
dateList.to_csv(csvfile)