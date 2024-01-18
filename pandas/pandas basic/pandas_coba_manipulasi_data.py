# -*- coding: utf-8 -*-
"""pandas coba manipulasi data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tIyd7svefiL-BkLAKQHVgd_-NC1plxEl
"""

import numpy as np
import pandas as pd

"""# Data"""

data_kategori = {
    'kategori_id':np.array([i for i in range(1,5)]),
    'ketagori':np.array(['makana','minuman','tambahan','kudapan']),
}

data_produk = {
    'kategori_id':np.array([1,1,1,2,2,2,1,3,2,3]),
    'produk':np.array([
        'Soto Ayam',
        'Nasi Goreng Seafood',
        'Sate Kambing',
        'Limun Soda',
        'Kopi Susu',
        'Air Mineral',
        'Bakso Sapi',
        'Tempe Bacem',
        'Es Teh Manis',
        'Kerupuk',
        ]),
}

"""# Operasi"""

kategori = pd.DataFrame(data_kategori)
produk = pd.DataFrame(data_produk)
gabung_table = pd.merge(produk,kategori, on='kategori_id')
gabung_table_outer = pd.merge(produk,kategori, on='kategori_id', how='outer')

"""# Sorting"""

urutkan = produk.sort_values(by='produk')
# urutkan = produk.sort_values(by='produk', ascending=False) # di balik urutannya
# urutkan_berdasarkan_index = produk.sort_index() # default nya gitu

df1 = pd.DataFrame([4,5,2,7,1,8], columns=['nilai'])
df1['ranking'] = df1['nilai'].rank()
print(df1)

"""# Binning 'Pecah data jadi bin(kecil)'"""

kelompok_usia = np.array([1,12,25,45,65])
kelompok_usia_label = np.array(['anak-anak','remaja','dewasa','lanjut usia'])
jumlah_data = 30
responden = np.array([i + np.random.randint(1,67) for i in range(jumlah_data)])

print(kelompok_usia)
print(kelompok_usia_label)
print(responden)

binning = pd.cut(responden, kelompok_usia, labels=kelompok_usia_label) # di bagi menjadi kecil berdasarkan label

data = {
    'kategori':binning,
    'usia':responden,
}


data_frame = pd.DataFrame(data).dropna()

print(binning, '\n')
print(data_frame, '\n')
pd.value_counts(binning)

"""# Tampilkan"""

print(kategori, '\n') # Data kategori
print(produk, '\n') # Data produk
print(gabung_table, '\n') # merge join
print(gabung_table_outer,'\n') # merge outer yang data Nan juga muncul
print(urutkan,'\n')