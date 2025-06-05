import pandas as pd
import numpy as np

sampleDataFrame=pd.DataFrame({"Adlar":["Selman","Osman","Mert Kemal"],"Yaşlar":[19,18,18],"Şehirler":["Bursa","Balıkesir","Balıkesir"]})
print(sampleDataFrame)

myArray=np.array(["Selman Yalçın","Mert Kemal Küreci","Osman Senih Demirci"])


sampleSerie=pd.Series(myArray)
sampleSerie2=pd.Series([10,20,30,40,50,60],index=[0,1,2,3,4,5])
print(sampleSerie,sampleSerie2)
print(sampleSerie[2],sampleSerie2[0])
sampleSerie2[0]="Selman Yalçın" #pandas seriesdeki bir değerideğiştirme
print(sampleSerie2)
sampleSerie2[6]="Never give up"#pandas seriese bir değer ekleme
print(sampleSerie2)
sampleSerie2=sampleSerie2.drop(3)#pandas seriesden veri çıkarma
print(sampleSerie2)


#dictionary yapısını kullanarak bir series oluşturma(Bence index ile tanımlamaktansa dictionary kullanmak çok daha temiz bir yol.)

myDictionary={"name":"Selman Yalçın","age":19,"country":"Turkey","major":"CS"}
selmanSerie=pd.Series(myDictionary)
selmanSerie["name"]="Selman"
print(selmanSerie)
selmanSerie=selmanSerie.drop("name")
print(selmanSerie)
selmanSerie["name"]="Selman"
selmanSerie["surname"]="Yalçın"
print(selmanSerie)

#sayısal bir series tanımlayalım

toeflAverages=pd.Series([23.93,21.72,20.73,19.82],index=["Reading","Listening","Speaking","Writing"])
print("Toplam:",toeflAverages.sum())#series içindeki tüm değerleri toplar
print("Ortlama:",toeflAverages.mean())#series içindeki değerlerin ortalamasını alır
print("Min:",toeflAverages.min())#series içindeki değerlerin minimumunu bulur
print("Max:",toeflAverages.max())#series içindeki değerlerin maksimumunu bulur
print(toeflAverages.index,toeflAverages.values,toeflAverages.dtype)

#pandas dataframes

toeflDataFrame=pd.DataFrame({"Reading":pd.Series([22,23,24,20,21,19],index=["Selman","Osman","Melih","Akif","İlker","Kemal"]),"Listening":[20,19,22,21,18,20],"Speaking":[17,16,17,18,20,21],"Writing":[15,18,29,20,22,19]})
print(toeflDataFrame)

#dataframe manipulation 

cupCounts=pd.DataFrame({
    "Teams":["Liverpool","Arsenal","Chelsea","Manchester United","Manchester City"],
    "Titles":[18,12,12,19,10],
    "CL Titles":[6,0,2,3,1]
})
print(cupCounts)
cupCounts["Location"]=["Liverpool","London","London","Manchester","Manchester"]#sütun ekleme
print(cupCounts)
print(cupCounts.iloc[0:4])#belli satırları çekme
print(cupCounts.loc[0:2])
cupCounts=cupCounts.drop(2)#satır silme
print(cupCounts)
cupCounts=cupCounts.drop("Location",axis=1)#sütun silme
print(cupCounts)
cupCounts.loc[4]=["Tottenham",0,0]#satır ekeleme
print(cupCounts)
print(cupCounts["Titles"])#bellir bir sütunun değerlerini çekme
cupCounts["Titles"]=[0,0,0,0]#sütunun değerlerini değiştirme
print(cupCounts)
cupCounts["Location"]=["Liverpool","London","Manchester","London"]
cupCounts.loc[0]=["Everton",0,0,"Merseyside Blue"]#hem ekleme hem satır değiştirme için kullanılabilir 
print(cupCounts)
cupCounts.loc["Chelsea"]=["Chelsea",0,3,"London"]
print(cupCounts.loc["Chelsea"])

#new dataframe (dictionary kullanarak tanımladım tıpkı series yapısında olduğu gibi burda da dictionary yapısını kullanmak çok daha efektif bir fikir çünkü çok daha kolay bir şekiklde index manipülasyonu yapmamıza olanak sağlıyor)

data={
    "Titles":[19,18,10,10],
    "CL Titles":[6,3,3,1],
    "Locations":["Liverpool","Manchester","London","Manchester"]
}

newTeamDf=pd.DataFrame(data,index=["Liverpool","Manchester United","Chelsea","Manchester City"])
print(newTeamDf)
print()
print(newTeamDf.loc["Liverpool"])
newTeamDf["FA Cup"]=[12,10,8,7]
newTeamDf.loc["Arsenal"]=[10,6,"London",20]
print(newTeamDf)
newTeamDf.loc["Tottenham"]=[0,0,"London",0]
print(newTeamDf)
newTeamDf=newTeamDf.drop("Tottenham")
print(newTeamDf)
newTeamDf=newTeamDf.drop("Locations",axis=1)
print(newTeamDf)

#csv dosyasından veri okuma

reviewContent=pd.read_csv("ReviewContent.csv")
print(reviewContent.head(20))#ilk n elemanı getirir 
print(reviewContent.info())
print()
print(reviewContent.tail()) # son n elemanı getirir
print()
print(reviewContent.ndim)# kaç satır kaç sütundan oluştuğu gibi verileri bize getirir
print()
print(reviewContent.dtypes)#sütunların altındaki verilerin bize türlerini döndürür
print("Daire Fiyatları Toplam",reviewContent["Room Price"].sum())#toplamlarını alma
print()
print("Daire Fiyatları Ortalama",reviewContent["Room Price"].mean())#ortlamalarını alma
print()
print(reviewContent["Room Price"].value_counts().head())
print()
print(reviewContent["Room Price"].sort_values(ascending=False))
mask=reviewContent["Room Type"]=="Private Room"
print(reviewContent)

#NaN verilerle çalışmak (numpy kütüphanesinin np.nan komutu sayesinde NaN veri tabloya eklenebilir)

data2={"Age":[18,18,np.nan],
       "Department":["CS",np.nan,"EE"],
       "Gender":[np.nan,np.nan,"F"]}
isNullDf=pd.DataFrame(data2,index=["Hale","Ahmet","Mehmet"])
print(isNullDf)#df yazma 
print()
print(isNullDf.isnull())#tablodaki değerlerin null olup olmadığını döndürür
print()
print(isNullDf.isnull().sum())#her bir sütun altında ne kadar null data olduğunu döndürür
print()
print(isNullDf.isnull().sum().sum())#dfde toplam kaç tane null data olduğunu iki tane sum art arda kullanarak görebiliriz.
print()
print(isNullDf.notnull())#isnull fonksiyonunun tersi şekilde çalışır
print()
print(isNullDf.notnull().sum())#birebir aynısı
print()
print(isNullDf.notnull().sum().sum())#birebir aynısı
print()
print(isNullDf.count())#notnull().sum() aynı işi yapar
print()
print(isNullDf.count().sum()) 
print(isNullDf.dropna())#herhangi bir değeri null olan herkesi kaldırır
print()
print(isNullDf.dropna(subset=["Gender"]))#belirli bir değeri null olanları kaldırır
print()
print(isNullDf.dropna(thresh=2))#
print()
print(isNullDf.fillna("Unknown"))#direk unknownu null olanlara bas geç
print()
print(isNullDf.fillna({"Age":18,"Department":"CS","Gender":"Attack Helicopter"}))#spesifik sütunlardaki null verileri fiks bir veri ile doldurma
print()
print(isNullDf.fillna(method="ffill"))#sütundaki bir sonraki datayı doldurur
print()
print(isNullDf.fillna(method="bfill"))#sütundaki bir önceki datayı doldurur
print()
print(isNullDf["Age"].fillna(method="ffill"))#ffilli spesifik bir sütun için kullanma