namakucing= 'ronald'
makanankucing = 'ikan'

def rubahnamakucing(namabaru):
    global namakucing
    namakucing=namabaru
    nama = namabaru
    print('nama kucing saya menjadi',namakucing)
def rubahmakanankucing(makanan,nama):
    global namakucing,makanankucing
    namakucing = nama
    makanankucing = makanan

rubahnamakucing('bibol')
rubahmakanankucing('nasi','wiski')
print('nama',namakucing,'makananaya',makanankucing)