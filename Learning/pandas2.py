import pandas as pd 
import numpy as np

review=pd.read_csv("ReviewContent.csv",usecols=["Room Price","Country","Room Price"])
print(review[review["Country"]=="United Kingdom"])
print()
print(review[(review["Room Price"]>60) & (review["Room Price"]<100)])# ve ile veri filtrelemek
print()
print(review[(review["Country"]=="United Kingdom") | (review["Country"]=="United States")])#ya da ile veri filtrelemek

#between ve duplicated kullanımı

review2=pd.read_csv("ReviewContent.csv",)
print(review2[review2["Review Date"].between("2013-01-01","2014-01-01")])#belli tarih aralıklarını bulmada kullanılabilir aynı zamanda belli aralıklar içinde ama operatörler yardımıyla bunu zaten yapabildiğimiz için ben gerek görmüyorum
print()
print(review2["City"].unique())#şehirlerin bir listesi
print(review2["City"].nunique())#şehirlerin kaç tane olduğu
print()
print(review2["City"].duplicated())
print(review2[review2["City"].duplicated()].head(10))#tekrar eden şehirlerin ilk 10 datası
print()
print(review2["City"].drop_duplicates())#tekrar eden verileri kaldırır