#fungsi dengan return value
def kuadrat(argumen):
    total = argumen**2
    print('nilai kuadrat dari',argumen,'yaitu',total)
    return total
x = kuadrat(9)
print(x)
print('-'*100)

def tambah(argumen1,argumen2):
    total= argumen1+argumen2
    print(total)
    return total
x = tambah(5,7)
print(x)
