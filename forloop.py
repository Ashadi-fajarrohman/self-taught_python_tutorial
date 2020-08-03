#list sebagai iterable
warna = ['merah','kuning','jingga','hijau','biru','nila','ungu','orange']

for i in warna:
    print(i)
    print(len(i))

# string sebagai iterable

pilih = 'merah'
for i in pilih:
    print(i)

# for dalam for

kulit = ['putih','coklat','sawo','hitam']
rambut = ['panjang','pendek','kriting','botak']

Data = [warna,kulit,rambut]

for subData in Data:
    print(subData)
    for komponen in subData:
        print(komponen)