# add your code here
# add your code here
import pandas as pd

flower = pd.DataFrame({'Apples': [35, 41], 'Bananas': [21, 34]}, index=['2017 Sales', '2018 Sales'])

flower.to_csv("fruit.csv", sep=',', encoding='utf-8', index=True)