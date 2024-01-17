import pandas as pd
import numpy as np
from faker import Faker



## series dan data frame
# series = kolom, data frame = table
apel = pd.Series([5,2,0,1])

## buat index sendiri
# jeruk = pd.Series([0,3,8,2], index=[1,2,3,4])
jeruk = pd.Series([0,3,8,2], index=['a','b','c','d'])

## Mengambil elemen
a = apel[1]
b = jeruk['d']

## Membuat data frame
data_frame1 = pd.DataFrame([3,2,0,1], columns=['apel'], index=[1,2,3,4])

pake_dict = {
    "apel": [5,2,0,1],
    'jeruk':[3,2,0,1]
}

data_frame2 = pd.DataFrame(pake_dict)

## menghitung jumlah elemen dengan fungsi count()
hasil = data_frame2.count()

## menghitung jumlah dari atas ke bawah
hasil2 = data_frame2.sum()

## fungsi statistik singkat tentang dataset (ini penting)
statistik = data_frame2.describe()

##Mengambil subset dari dataframe
# apel = data_frame1.apel
# apel = data_frame2["jeruk"]

a = jeruk[:2]
b = apel[2:]
c = data_frame2['jeruk']>2
d = data_frame2[data_frame2['jeruk']>2]
## menampilkan kepala doang
e = data_frame2.head(2)

# jeruk_apel = data_frame2[['apel','jeruk']]
## tranpose data
f = data_frame2.T
## menggunakan Index
g = data_frame2.iloc[3]
h = data_frame2.iloc[[3,1]] # multiple indexing
i = data_frame2.iloc[3,[1,0]] # menampilkan subset data berindex=3 kolom 1 dan kolom 0

dict1 = {
    'apel':[5,2,0,1],
    'jeruk':[0,3,8,2]
}
df3 = pd.DataFrame(dict1, index=['a','b','c','d'])
j = df3.loc['c']

## Deleting 
del1 = df3.drop('b') # menghapus baris (tapi yang asli tidak terhapus) dan memasukan ke variable del1
df3.drop('b', inplace=True) # menghapus baris permanen inplace=True
# lihat perubahan
# print(df3)

df4 = pd.DataFrame([1,2,2,3,4,3,5,5,6,7,8,9,3],columns=['Nilai'])

## menghilangkan data duplicate
k = df4.duplicated() # tipe true berarti duplicate
## menghapus data duplicate
duplikasi_di_hapus = df4.drop_duplicates(keep='first') # keep first berarti data selain yang awal(asli) di hapus. ada lg yg lain(keep='last')
l = df4.drop_duplicates(['Nilai'], keep='first') # ini lebih spesifik dgn kolom "Nilai"

## data frame mengubah data kosong menjadi Nan atau angka(999)
df1 = pd.DataFrame([1,2,None,4,5,None], columns=['nilai'])
## membuang data kosong
hapus_data_kosong = df1.dropna() # aslinya tidak di ubah
ganti_data_kosong_jadi_angka = df1.fillna(999)
# print(ganti_data_kosong_jadi_angka)



""" Kasus Manipulasi Data dengan ranmdom dan program kelulusan """
"""ingat incase sensitive setiap key, value"""


fake = Faker()

jumlah_data = 10


data = {
    'nama':[fake.name() for _ in range(jumlah_data)],
    'nilai':np.array([i + np.random.randint(20,99) for i in range(jumlah_data)])
}

data_frame = pd.DataFrame(data, index=[i for i in range(1,11)])


### cara 1 ###
# data_frame['kelulusan'] = data_frame['nilai'].apply(lambda x: 'lulus' if x >=60 else 'gagal')

# >> buat data null
data_frame['Kelulusan'] = ''

for index, row in data_frame.iterrows():
    if row['nilai'] >= 60:
        data_frame.at[index, 'Kelulusan'] = "lulus"
    else:
        data_frame.at[index, 'Kelulusan'] = "gagal"


deskrips_data_frame = data_frame.describe()
# Output
print(data_frame)
print(deskrips_data_frame)