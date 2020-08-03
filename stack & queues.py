#perbedaan stack & queues, stack keluar yang diakhir (analogi tumpukan buku) queues keluar yang didpan(analogi antri makanan)
#stack=tumpukan
#queues=antrian

tumpukan = [1,2,3,4,5,6]
print('data sekarang',tumpukan)
tumpukan.append(7)
print('data masuk:',7)
print('data sekarang',tumpukan)

tumpukan.pop()
print('data sekarang',tumpukan)
print('-'*100)
print('queues/antrian')

from collections import deque

antrian = deque([1,2,3,4,5])
print('data sekarang:',antrian)
antrian.append(6)
print('data masuk:',6)
print('data sekarang',antrian)
antrian.append(7)
print('data masuk',7)
print('data sekarang',antrian)

#mengurangi antrian
out= antrian.popleft()
print('data keluar',out)
print('data sekarang',antrian)