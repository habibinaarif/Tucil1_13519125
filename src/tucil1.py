import time

def konversi(kata, subs):
    s=''
    for huruf in kata:
        idx=subs[0].index(huruf)
        idx=subs[0].index(huruf)
        s=s+str(subs[1][idx])
    return int(s)

def permut(arr,n):
    if n<=0:
        return[[]]
    dummy=[]
    for i in range(len(arr)):
        current=arr[i]
        remain=arr[:i]+arr[i+1:]
        for p in permut(remain,n-1):
            dummy.append([current]+p)
    return dummy

namafile = input("Masukkan nama file: ")
f = open(namafile)

start = time.time()
data = f.read()
baris = data.split()

hasil=[]
for huruf in baris[len(baris)-1]:
    hasil.append(huruf)

operan=[]
for i in range(len(baris)-3):
    dummy=[]
    for huruf in baris[i]:
        dummy.append(huruf)
    operan.append(dummy)

dummy=[]
for i in range(len(baris[len(baris)-3])-1):
    dummy.append(baris[len(baris)-3][i])
operan.append(dummy)

huruf=operan+list(hasil)
union=sorted(list(set().union(*huruf)))

angka=[0,1,2,3,4,5,6,7,8,9]
counter=0
solusi=False

for p in permut(angka,len(union)):
    counter+=1
    subs=[union]+[p]
    if (sum(konversi(opr,subs) for opr in operan) == konversi(hasil,subs)) and (konversi(op,subs) >= pow(10,len(op)-1) for op in operan) and (konversi(hasil,subs) >= pow(10,len(hasil)-1)):
        solusi=True
        break;

end=time.time()

print(data)
print()
if solusi:
    for i in range(len(operan)-1):
        print(konversi(operan[i],subs))
    print(konversi(operan[len(operan)-1],subs),end='+\n')
    print('------')
    print(konversi(hasil,subs))
else:
    print("Tidak ada solusi")
print()
print("Waktu eksekusi programnya adalah "+str(end-start))
print("Total tes yang dilakukan adalah "+str(counter))