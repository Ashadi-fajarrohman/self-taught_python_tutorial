Data = [1,4,9,25,36,49,64,81,100]

# mengakses list
Subdata = Data[5]
Subdata1 = Data[-3]

# memotong list
Subdata2 = Data[1:5]
Subdata3 = Data[:4]
Subdata4 = Data[5:]

Data2 = [5,10,15,20,25,30,35,40,45,50]

# menambah list
Data3 = Data + Data2

# merubah data dalam list
Data[4] = 50

# mengcopy list ke variable baru
a = Data[:]
a[4] = 70

# merubah content list dengan metode slicing
Data[2:5] = [10,20,30]

# list dalam list (multidimensional list)
x = [Data, Data2]

# mengakses list dalam multidimensional list
y = x[0][4]
y = x[1][7]

# methode untukk list
Data2.append(63)

# Function untuk list
panjang_list = len(Data3)
print(Data3)
print(panjang_list)
