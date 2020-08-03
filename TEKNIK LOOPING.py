#TEKNIK LOOPING

nama_band = ['ungu','wali','peterpan','kotak']
warna = ['merah',
         'kuning',
         'hijau',
         'biru']
#enumerate=>untuk mengindeks

for i, band in enumerate(nama_band):
    print(i,':',band)

#zip=>untuk memasangkan
for band,warna in zip(nama_band,warna):
    print(band,'berwarna:',warna)

#sorted=>buat ngurutin abjad
data = ['hadir','alfa','izin','sakit']
for absensi in sorted(data):
    print(absensi)

#dictionary
playlist={'air':'biru','tanah':'coklat','api':'merah'}
for i,v in playlist.items():
    print(i,v)
