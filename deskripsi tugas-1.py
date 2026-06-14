#Data mahasiswa
data_mahasiswa = [
   
    ["neza",  95],
    ["rhido", 75],
    ["sahdik",90],
    ["riski", 85],
    ["habib", 98],
    ["aldo",  65],
    ["sandi", 68],
    ["lale",  92],
    ["rofal", 90],
    ["gazi",  90],
    ["rifi",  89],
    ["ciba",  98],
    ["pina",  90],
    ["diah",  95]
]

print("==============================")
print(" APLIKASI MANAJEMEN NILAI MAHASISWA")
print("==============================")
print()

# Mengurutkan berdasarkan nilai tertinggi

data_mahasiswa.sort(key=lambda x: x[1], reverse=True)

print("Data Mahasiswa Berdasarkan Nilai Tertinggi")
print("-----------------------------------------")

for i, data in enumerate(data_mahasiswa, start=1):
    print(f"{i}. Nama : {data[0]} | Nilai : {data[1]}")