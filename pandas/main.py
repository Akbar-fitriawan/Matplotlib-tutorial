from faker import Faker
import numpy as np
import pandas as pd

fake = Faker()

jumlah_baris = 10
jumlah_kolom = 1

data = {
    'Nama':[fake.name() for _ in range(jumlah_baris)],
    'Nilai':np.array([i + np.random.randint(20,90) for i in range(jumlah_baris)])
}

df = pd.DataFrame(data)

print(df)
deskripsi = df.describe()
print(deskripsi)