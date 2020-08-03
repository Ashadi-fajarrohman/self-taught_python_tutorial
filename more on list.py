barang = ['kunci','ember','tang','mobil','motor']
print(barang)

#beberapa method untuk memanipulasi list
barang.append('galon')
print(barang)

barang.extend('sepeda')
print(barang)

barang.insert(3,'sepeda')
print(barang)

#method untuk menhitung anggota
jumlahsepeda = barang.count('sepeda')
print('jumlah sepeda adalah:',jumlahsepeda)

#remove data = memindahkan barang yangb pertama kali muncul
barang.remove('tang')
print(barang)

barang.reverse()
print(barang)

stuff=barang
stuff.append('bekel')
print(stuff)